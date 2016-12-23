#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simplify tags of the input file IN-PLACE as described in
   README.md. The input file should contain words of only one
   part-of-speech (POS) category and the POS should be specified.
"""
from __future__ import unicode_literals, division, print_function #Py2

__author__ = "Daniel van Niekerk"
__email__ = "dvn.demitasse@gmail.com"

import re


POS_INOUT = {"adj": {"in": {"ar"},
                     "out": {}},
             "adv": {"in": {"ar", "vr", "nr"},
                     "out": {}},
             "conj": {"in": {},
                      "out": {}},
             "cop": {"in": {"ar", "vr", "nr", "p1_vr"},
                     "out": {"vpl", "locsf", "dim", "aug", "fem"}}, #check again after VERB
             "dem": {"in": {"vr", "nr", "p1_vr"},
                     "out": {"fem"}},
             "intj": {"in": {},
                      "out": {}},
             "loc": {"in": {"ar", "vr", "nr"},
                     "out": {"locsf", "dim", "aug", "fem"}}, #check again after VERB
             "noun": {"in": {"ar", "vr", "nr", "p1_vr"},
                      "out": {"vpl", "vps", "rsf", "locsf", "dim", "aug", "fem"}},
             "pos": {"in": {"ar", "vr", "nr", "p1_vr"},
                     "out": {"vpl", "vps", "rsf", "imp", "locsf", "dim", "fem"}},
             "prep": {"in": {"ar", "vr", "nr", "p1_vr"},
                      "out": {"vpl", "vps", "rsf", "locsf", "dim", "aug", "fem"}}, #check again after VERB
             "pres": {"in": {},
                      "out": {}},
             "pron": {"in": {"ar"},
                      "out": {}},
             "rel": {"in": {"ar", "vr", "nr", "p1_vr"},
                     "out": {"vpl", "vps", "rsf", "imp", "locsf", "dim", "fem"}},
             "unk": {"in": {"ar", "vr", "nr", "p1_vr"},
                     "out": {"locsf", "dim", "aug", "fem"}},
             "verb": {"in": {"ar", "vr", "nr", "p1_vr", "i6_vr", "s6_vr"},
                      "out": {"vpl", "vps", "vpn", "rsf", "imp", "locsf", "vpg"}}
}

if __name__ == "__main__":
    import argparse, sys, codecs
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('fn', metavar='FN', type=str, help="input/output filename")
    parser.add_argument('pos', metavar='POS', type=str, help="Part-of-speech")
    args = parser.parse_args()

    with codecs.open(args.fn, encoding="utf-8") as infh:
        lines = infh.read().splitlines()

    pos = args.pos
    re_in = re.compile("<({})>".format("|".join(POS_INOUT[pos]["in"])))
    re_out = re.compile("<({})>".format("|".join(POS_INOUT[pos]["out"])))
    re_tag = re.compile("<.+?>")
    with codecs.open(args.fn, "w", encoding="utf-8") as outfh:
        for line in lines:
            word, fields = line.split("\t")
            #print(word)
            parses = [f.strip(",") for f in fields.split()]
            for i, p in enumerate(parses):
                p = "<{}>".format(pos) + p
                #ins and outs...
                p = re_in.sub("{", p)
                p = re_out.sub("}", p)
                #remove others...
                p = re_tag.sub("", p)
                p = p.replace("{}", "")
                #cleanup
                for m in reversed(list(re.finditer("{", p))[1:]):
                    p = p[:m.start()] + p[m.end():]
                for m in reversed(list(re.finditer("}", p))[:-1]):
                    p = p[:m.start()] + p[m.end():]
                if "{" in p and not "}" in p:
                    p = p + "}"
                if "}" in p and not "{" in p:
                    p = p.replace("}", "")
                #update
                parses[i] = p
            outfh.write("{}\t{}\n".format(word, ", ".join(set(parses))))
