#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Swap the tag order of the file IN-PLACE
"""
from __future__ import unicode_literals, division, print_function #Py2

import re

import numpy as np

if __name__ == "__main__":
    import sys

    pos = sys.argv[1]
    
    r = re.compile("{.+?}")
    
    for line in sys.stdin:
        line = unicode(line, encoding="utf-8")
        word, fields = line.split("\t")
        #print(word)
        parses = [f.strip(",") for f in fields.split()]
        parse = parses[np.argmax([len(r.sub("", p)) for p in parses])]
        print("\t".join([word, pos, parse]).encode("utf-8"))
