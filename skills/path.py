# -*- coding: utf-8 -*-
import os
__author__ = 'kong90'


def tree(top):
    # path, folder list, file list
    for path, names, fnames in os.walk(top):
        for fname in fnames:
            yield os.path.join(path, fname)


for name in tree(os.getcwd()):
    print name