#!/bin/zsh
cd "/Users/admin/Downloads/New short/product-explainer"
./scripts/run_full_queue.sh
./scripts/retake_pass.sh
echo "[all] generation + retakes finished $(date '+%H:%M:%S')"
