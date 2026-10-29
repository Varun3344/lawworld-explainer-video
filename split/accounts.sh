# Resolve SPLIT_ACCOUNT (a slot name) into SPLIT_UD, the signed-in Flow browser profile to render on.
# Sourced by split/<set>_env.sh, always from the repo root.
#
# The slot -> profile mapping is machine-local and is NEVER committed: the directories hold live Google
# login sessions, and naming the accounts in public ties them to this automation. Copy
# split/accounts.example.sh to split/accounts.local.sh and fill in your own profile directories.
[ -f split/accounts.local.sh ] && . split/accounts.local.sh
eval "SPLIT_UD=\${FLOW_UD_${SPLIT_ACCOUNT:-main}:-}"
export SPLIT_UD
[ -n "$SPLIT_UD" ] || echo "[accounts] no Flow profile for slot '${SPLIT_ACCOUNT:-main}' - see split/accounts.example.sh" >&2
