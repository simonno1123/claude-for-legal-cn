#!/usr/bin/env bash
# Install the privacy guard as this clone's git pre-commit hook (local only; hooks are not committed).
# The private term list stays outside the repository: either point PRIVACY_GUARD_TERMS at it,
# or copy it to .git/privacy_guard_terms.txt in this clone (inside .git, so it is never committed).
set -euo pipefail
root="$(git rev-parse --show-toplevel)"
hook="$root/.git/hooks/pre-commit"
cat > "$hook" <<'HOOK'
#!/usr/bin/env bash
root="$(git rev-parse --show-toplevel)"
terms="${PRIVACY_GUARD_TERMS:-$root/.git/privacy_guard_terms.txt}"
if [ -f "$terms" ]; then
  exec python3 "$root/scripts/privacy_guard/check_public_text.py" --staged --terms "$terms"
fi
exec python3 "$root/scripts/privacy_guard/check_public_text.py" --staged
HOOK
chmod +x "$hook"
echo "installed $hook (private term list: ${PRIVACY_GUARD_TERMS:-not set})"
