# Simplification of labelled word list

This directory contains a set of scripts used to simplify the manually
labelled word list `../2010.07.17.WordListLabelled.txt` to identify
open-class ("content") morphemes (in curly braces).

To create a sorted dictionary with POS tags and "parses" do:

```
bash do.sh | sort -k 1 > dict.tsv
```
