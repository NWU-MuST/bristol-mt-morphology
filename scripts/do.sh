#!/bin/bash

TMPDIR=tmp #`mktemp -d`

mkdir $TMPDIR
python ../posTagger.py -i ../2010.07.17.WordListLabelled.txt -o $TMPDIR/words.pos -s

for fn in $TMPDIR/words.pos.*; do
    ./swaptagorder.py $fn
done

