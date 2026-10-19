#!/bin/zsh
# Runs split/post_course.sh for the course sets one after another (the Mac renders one video's post-production at a time).
# Usage: zsh split/post_queue.sh set:stem [set:stem ...]
cd "/Users/admin/Downloads/New short/product-explainer"
for x in "$@"; do s=${x%%:*}; stem=${x#*:}; zsh split/post_course.sh $s $stem; done
echo "[post] ALL DONE $(date +%H:%M:%S)"
