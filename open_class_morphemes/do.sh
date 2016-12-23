#!/bin/bash

TMPDIR=`mktemp -d`

python ../posTagger.py -i ../2010.07.17.WordListLabelled.txt -o $TMPDIR/words.pos -s

for fn in $TMPDIR/words.pos.*; do
    ./swaptagorder.py $fn
done

for pos in adj adv conj cop dem intj loc noun pos prep pres pron rel unk verb; do
    ./simplifytags.py $TMPDIR/words.pos.$pos $pos
done

for pos in adj adv conj cop dem intj loc noun pos prep pres pron rel unk verb; do
    cat $TMPDIR/words.pos.$pos | ./disambigwords.py $pos
done

rm -fr $TMPDIR

