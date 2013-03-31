#!/usr/bin/env python
# coding: utf-8

#http://kshi-kshi.hateblo.jp/entry/2012/02/02/220354

import os
import sys
import stat

DIR_PATH = "/Users/tell_k/Work/code-snippets/python/snippets/hogehoge"
RENAME_PATTERN = "IMG_%05d%s"

if __name__ == "__main__":
    if not os.path.isdir(DIR_PATH):
        sys.exit("ERROR: '%s' is not directory." % DIR_PATH)

    index = 0
    (root, dirs, files) = next(os.walk(DIR_PATH.rstrip(os.sep)))
    targets = dict([(os.stat(os.path.join(root, f)).st_ctime, f) for f in files])
    for st_ctime, filename in sorted(targets.items()):
        index += 1
        (name, ext) = os.path.splitext(filename)
        os.rename(os.path.join(root, filename), os.path.join(root, RENAME_PATTERN % (index, ext)))
