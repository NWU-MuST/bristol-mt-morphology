#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Swap the tag order of the file IN-PLACE
"""
from __future__ import unicode_literals, division, print_function #Py2

import re

if __name__ == "__main__":
    import sys, codecs

    r = re.compile("<.+?>")

    with codecs.open(sys.argv[1], encoding="utf-8") as infh:
        lines = infh.read().splitlines()

    with codecs.open(sys.argv[1], "w", encoding="utf-8") as outfh:
        for line in lines:
            word, fields = line.split("\t")
            parses = [f.strip(",") for f in fields.split()]
            for i, p in enumerate(parses):
                pp = ""
                for a, b in zip(r.findall(p), r.split(p)):
                    pp += a+b
                parses[i] = pp
            outfh.write("{}\t{}\n".format(word, ", ".join(parses)))
