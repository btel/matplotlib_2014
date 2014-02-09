#!/usr/bin/env python
#coding=utf-8

import os
import sys

import matplotlib

matplotlib.rcParams['backend'] = 'Agg'

import matplotlib.pyplot as plt

if __name__ == "__main__":

    import sys

    script = sys.argv[1]
    outdir = sys.argv[2]
    
    script_path, script_name = os.path.split(script)
    
    execfile(script)

    root, ext = os.path.splitext(script_name)

    fname = root + '.png'
    path = os.path.join(outdir, fname)
    plt.savefig(path)
