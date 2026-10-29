# Template for split/accounts.local.sh (gitignored).
# One entry per signed-in Flow browser profile; FLOW_UD_<slot> is the profile directory that
# `npm run login` in the Flow pipeline created. The <set>_env.sh files only ever name the slot.
FLOW_ACCOUNTS="$HOME/Library/Application Support/LawWorld/flow-accounts"
FLOW_UD_main="$FLOW_ACCOUNTS/my-first-account"
FLOW_UD_a1="$FLOW_ACCOUNTS/my-second-account"
FLOW_UD_a2="$FLOW_ACCOUNTS/my-third-account"
FLOW_UD_a3="$FLOW_ACCOUNTS/my-fourth-account"
