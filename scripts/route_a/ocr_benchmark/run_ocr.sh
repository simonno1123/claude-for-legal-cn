#!/usr/bin/env bash
# Route A Tesseract chi_sim benchmark runner (design: TASK_PHASE2_ROUTE_A_TESSERACT_CHI_SIM_BENCHMARK_DESIGN, confirmed).
# Output formats are set with -c parameters: the private tessdata directory has no configs/ folder, so the "txt tsv" config names would not load.
# Recognition runs inside a bwrap sandbox with no network and only whitelisted mounts; evidence is recorded.
# The host only allows short foreground calls, so the run is split into phases on one run directory:
#   run_ocr.sh <root> <set> <run_id> init          network-denial evidence, write-scope snapshot, environment record
#   run_ocr.sh <root> <set> <run_id> batch <N>     recognise up to N not-yet-processed images within a time budget (BUDGET, default 100 s) (each batch re-checks network denial)
#   run_ocr.sh <root> <set> <run_id> finish        input-handling checks, stop checks (outbound attempts, write scope)
set -euo pipefail
ROOT="$1"; SET="$2"; RUN="$3"; PHASE="$4"; N="${5:-8}"
TESS="$ROOT/../tessdata"
SAMPLES="$ROOT/$SET/samples"
INPUTS="$ROOT/$SET/inputs"
OUT="$ROOT/runs/$RUN"
PRIV="$(cd "$ROOT/../.." && pwd)"
[ -f "$TESS/chi_sim.traineddata" ] || { echo "STOP: chi_sim.traineddata missing"; exit 2; }

BINDS=(--unshare-net --die-with-parent --proc /proc --dev /dev --tmpfs /tmp)
for d in /usr /lib /lib64 /bin /sbin /etc; do [ -e "$d" ] && BINDS+=(--ro-bind "$d" "$d"); done
BINDS+=(--ro-bind "$TESS" /tessdata --ro-bind "$SAMPLES" /samples --ro-bind "$INPUTS" /inputs --bind "$OUT" /out --chdir /out)

net_denied() {  # evidence: the sandbox cannot reach the network (must fail)
  if bwrap "${BINDS[@]}" curl -sS -m 5 https://example.com -o /dev/null 2>> "$OUT/net_check.txt"; then
    echo "STOP: sandbox reached the network"; exit 3
  fi
  echo "[$(date -Iseconds)] network denied" >> "$OUT/net_check.txt"
}
snapshot() { find "$PRIV" -path "$OUT" -prune -o -type f -printf '%p %s %T@\n' | sort; }
traced() {  # run inside the sandbox, tracing network-related syscalls into a per-call file
  strace -f -qq -e trace=connect,sendto,socket -o "$OUT/strace_network_$(date +%s%N).txt" bwrap "${BINDS[@]}" "$@"
}

case "$PHASE" in
init)
  [ ! -e "$OUT" ] || { echo "STOP: run directory exists (no overwrite)"; exit 2; }
  mkdir -p "$OUT/ocr" "$OUT/inputs"
  net_denied
  snapshot > "$OUT/.files_before"
  {
    echo "tesseract: $(tesseract --version 2>&1 | head -1)"
    echo "chi_sim_sha256: $(sha256sum "$TESS/chi_sim.traineddata" | cut -d' ' -f1)"
    echo "samples_manifest_sha256: $(sha256sum "$ROOT/$SET/manifest.json" | cut -d' ' -f1)"
    echo "params: -l chi_sim --psm 3 --oem 1 -c tessedit_create_txt=1 -c tessedit_create_tsv=1"
    echo "start: $(date -Iseconds)"
  } > "$OUT/run_env.txt"
  echo "OK: init" ;;
batch)
  [ -f "$OUT/run_env.txt" ] || { echo "STOP: run not initialised"; exit 2; }
  net_denied
  todo=()
  for f in "$SAMPLES"/*.png; do b=$(basename "$f" .png); [ -f "$OUT/ocr/$b.tsv" ] || todo+=("$b"); done
  [ ${#todo[@]} -gt 0 ] || { echo "OK: nothing left"; exit 0; }
  list=("${todo[@]:0:$N}")
  DL=$(( $(date +%s) + ${BUDGET:-100} ))  # no new image is started after the time budget (host calls are cut off at about 180 s)
  traced bash -c '
    DL="$1"; shift
    for b in "$@"; do
      [ "$(date +%s)" -lt "$DL" ] || break
      s=$(date +%s%N)
      tesseract "/samples/$b.png" "/out/ocr/$b" -l chi_sim --psm 3 --oem 1 --tessdata-dir /tessdata -c tessedit_create_txt=1 -c tessedit_create_tsv=1 >/dev/null 2>>/out/ocr/_stderr.txt || echo "$b FAILED" >> /out/ocr/_failed.txt
      e=$(date +%s%N); echo "$b $(( (e - s) / 1000000 ))ms" >> /out/ocr/_timing.txt
    done' _ "$DL" "${list[@]}"
  done_n=0
  for b in "${list[@]}"; do grep -q "^$b " "$OUT/ocr/_timing.txt" 2>/dev/null || continue; done_n=$((done_n+1)); [ -s "$OUT/ocr/$b.tsv" ] && [ -f "$OUT/ocr/$b.txt" ] || { echo "STOP: $b produced no txt/tsv output"; exit 6; }; done
  echo "OK: batch $done_n done, $(( ${#todo[@]} - done_n )) left" ;;
finish)
  net_denied
  left=0; for f in "$SAMPLES"/*.png; do b=$(basename "$f" .png); [ -f "$OUT/ocr/$b.tsv" ] || left=$((left+1)); done
  [ "$left" -eq 0 ] || { echo "STOP: $left images not processed"; exit 2; }
  traced bash -c '
    pdftotext -f 1 -l 1 /inputs/hybrid.pdf /out/inputs/hybrid_p1_native.txt 2>>/out/inputs/_stderr.txt; echo "hybrid_p1_native rc=$?" >> /out/inputs/_rc.txt
    n=$(pdftotext -f 2 -l 2 /inputs/hybrid.pdf - 2>/dev/null | tr -d "[:space:]" | wc -c); echo "hybrid_p2_native_chars=$n" >> /out/inputs/_rc.txt
    pdftoppm -f 2 -l 2 -r 300 -png /inputs/hybrid.pdf /out/inputs/hybrid_p2 2>>/out/inputs/_stderr.txt
    tesseract /out/inputs/hybrid_p2-2.png /out/inputs/hybrid_p2_ocr -l chi_sim --psm 3 --tessdata-dir /tessdata >/dev/null 2>&1; echo "hybrid_p2_ocr rc=$?" >> /out/inputs/_rc.txt
    for f in truncated.pdf encrypted.pdf; do pdfinfo "/inputs/$f" >/dev/null 2>>/out/inputs/_stderr.txt; echo "$f pdfinfo rc=$?" >> /out/inputs/_rc.txt; done
    echo "unsupported file type: $(file -b /inputs/unsupported.xyz)" >> /out/inputs/_rc.txt
    tesseract /inputs/unsupported.xyz /out/inputs/unsupported -l chi_sim --tessdata-dir /tessdata >/dev/null 2>>/out/inputs/_stderr.txt; echo "unsupported tesseract rc=$?" >> /out/inputs/_rc.txt'
  echo "end: $(date -Iseconds)" >> "$OUT/run_env.txt"
  if cat "$OUT"/strace_network_*.txt | grep -E 'connect\(.*(AF_INET|AF_INET6)' > "$OUT/outbound_attempts.txt"; then
    echo "STOP: outbound connection attempt recorded; results void"; exit 4
  fi
  snapshot > "$OUT/.files_after"
  if ! diff -q "$OUT/.files_before" "$OUT/.files_after" >/dev/null; then
    diff "$OUT/.files_before" "$OUT/.files_after" > "$OUT/write_scope_violation.txt" || true
    echo "STOP: files outside the run directory changed; results void"; exit 5
  fi
  echo "OK: run $RUN complete" ;;
*) echo "unknown phase"; exit 2 ;;
esac
