#!/usr/bin/env bash
# Route A Tesseract chi_sim benchmark runner (design: TASK_PHASE2_ROUTE_A_TESSERACT_CHI_SIM_BENCHMARK_DESIGN, confirmed).
# Output formats are set with -c parameters: the private tessdata directory has no configs/ folder, so the "txt tsv" config names would not load.
# Recognition runs inside a bwrap sandbox with no network and only whitelisted mounts; evidence is recorded.
# The host only allows short foreground calls, so the run is split into phases on one run directory:
#   run_ocr.sh <root> <set> <run_id> selftest      deliberate outbound attempt in a throwaway run; must be detected and locked
#   run_ocr.sh <root> <set> <run_id> init          network-denial evidence, write-scope snapshot, environment record
#   run_ocr.sh <root> <set> <run_id> batch <N>     recognise up to N not-yet-processed images within a time budget (BUDGET, default 100 s) (each batch re-checks network denial)
#   run_ocr.sh <root> <set> <run_id> finish        input-handling checks, final stop checks (outbound attempts, write scope)
# Network syscalls are watched while each sandboxed call runs; the first outbound attempt kills it and locks the run as void.
set -euo pipefail
ROOT="$1"; SET="$2"; RUN="$3"; PHASE="$4"; N="${5:-8}"
TESS="$ROOT/../tessdata"
SAMPLES="$ROOT/$SET/samples"
INPUTS="$ROOT/$SET/inputs"
OUT="$ROOT/runs/$RUN"
PRIV="$(cd "$ROOT/../.." && pwd)"
[ -f "$TESS/chi_sim.traineddata" ] || { echo "STOP: chi_sim.traineddata missing"; exit 2; }

# /dev is a minimal sandbox-private device tree (null, zero, random ...); /tmp is mapped into the run directory, so
# every writable path the recognition process can see lies inside the audited run directory.
BINDS=(--unshare-net --die-with-parent --proc /proc --dev /dev)
for d in /usr /lib /lib64 /bin /sbin /etc; do [ -e "$d" ] && BINDS+=(--ro-bind "$d" "$d"); done
BINDS+=(--ro-bind "$TESS" /tessdata --ro-bind "$SAMPLES" /samples --ro-bind "$INPUTS" /inputs --bind "$OUT" /out --bind "$OUT/tmp" /tmp --setenv TMPDIR /tmp --chdir /out)

net_denied() {  # evidence: the sandbox cannot reach the network (must fail)
  if bwrap "${BINDS[@]}" curl -sS -m 5 https://example.com -o /dev/null 2>> "$OUT/net_check.txt"; then
    echo "STOP: sandbox reached the network"; exit 3
  fi
  echo "[$(date -Iseconds)] network denied" >> "$OUT/net_check.txt"
}
snapshot() { find "$PRIV" -path "$OUT" -prune -o -type f -printf '%p %s %T@\n' | sort; }
# Any network-family syscall other than local (AF_UNIX / AF_NETLINK) sockets counts as an outbound attempt.
ATTEMPT='(socket\((AF_INET|AF_INET6|AF_PACKET)|(connect|sendto|sendmsg|sendmmsg)\(.*(AF_INET|AF_INET6|AF_PACKET))'
void_lock() { echo "[$(date -Iseconds)] $1" >> "$OUT/VOID_LOCK"; echo "STOP: $1; results void"; exit 4; }
traced() {  # run inside the sandbox; all network syscalls traced; watched while running, killed at the first attempt
  local log="$OUT/strace_network_$(date +%s%N).txt"
  strace -f -qq -e trace=%network -o "$log" bwrap "${BINDS[@]}" "$@" &
  local pid=$!
  while kill -0 "$pid" 2>/dev/null; do
    if grep -Eq "$ATTEMPT" "$log" 2>/dev/null; then kill -KILL "$pid" 2>/dev/null; pkill -KILL -f "^tesseract " 2>/dev/null || true
      grep -E "$ATTEMPT" "$log" >> "$OUT/outbound_attempts.txt"; void_lock "outbound network attempt during run"; fi
    sleep 0.2
  done
  wait "$pid" || true
  if grep -Eq "$ATTEMPT" "$log"; then grep -E "$ATTEMPT" "$log" >> "$OUT/outbound_attempts.txt"; void_lock "outbound network attempt during run"; fi
}

[ ! -f "$OUT/VOID_LOCK" ] || { echo "STOP: run is void (VOID_LOCK)"; exit 4; }
case "$PHASE" in
selftest)  # proves the watcher fires: a deliberate outbound attempt in a throwaway run directory must lock it as void
  [ ! -e "$OUT" ] || { echo "STOP: run directory exists (no overwrite)"; exit 2; }
  mkdir -p "$OUT/tmp"
  ( traced curl -sS -m 5 https://example.com -o /dev/null ) && { echo "SELFTEST FAILED: attempt not detected"; exit 7; }
  [ -f "$OUT/VOID_LOCK" ] || { echo "SELFTEST FAILED: no VOID_LOCK"; exit 7; }
  echo "SELFTEST OK: attempt detected and run locked"; exit 0 ;;
init)
  [ ! -e "$OUT" ] || { echo "STOP: run directory exists (no overwrite)"; exit 2; }
  mkdir -p "$OUT/ocr" "$OUT/inputs" "$OUT/tmp"
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
  if cat "$OUT"/strace_network_*.txt | grep -E "$ATTEMPT" > "$OUT/outbound_attempts_final.txt"; then void_lock "outbound network attempt recorded"; fi
  grep -c . "$OUT"/strace_network_*.txt > "$OUT/strace_line_counts.txt" || true
  snapshot > "$OUT/.files_after"
  if ! diff -q "$OUT/.files_before" "$OUT/.files_after" >/dev/null; then
    diff "$OUT/.files_before" "$OUT/.files_after" > "$OUT/write_scope_violation.txt" || true
    echo "[$(date -Iseconds)] files outside the run directory changed" >> "$OUT/VOID_LOCK"
    echo "STOP: files outside the run directory changed; results void"; exit 5
  fi
  find "$OUT/tmp" -type f | sed "s#^$OUT/##" > "$OUT/tmp_files.txt"
  echo "OK: run $RUN complete" ;;
*) echo "unknown phase"; exit 2 ;;
esac
