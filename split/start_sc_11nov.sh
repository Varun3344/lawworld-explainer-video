#!/bin/zsh
# 11-11-2026 SC batch (owner "YES start doing"): 8 HOOK-format Supreme Court reels, 2 per Flow account, lanes staggered 60 s.
# main: anc -> ocl | a1: bhk -> ack | a2: prr -> nbt | a3: spc -> cmr. The 06-11 dispatcher (split/post_batch_06nov.sh, reads
# split/batch_06nov.tsv) flattens, posts, makes the darkfoot thumbnail, QAs and ships each set once its queue says ALL DONE.
cd "/Users/admin/Downloads/New short/product-explainer"
lane() { local a=$1 b=$2
  ( source split/${a}_env.sh && python3 split/make_course_sb.py $a --new-project && touch split/GO$a && zsh split/run_queue.sh c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 ) > logs/queue_$a.log 2>&1
  zsh split/chain_after.sh $a $b > logs/queue_$b.log 2>&1
}
lane anc ocl &!
sleep 60; lane bhk ack &!
sleep 60; lane prr nbt &!
sleep 60; lane spc cmr &!
echo "all 4 lanes started $(date +%H:%M:%S)"
