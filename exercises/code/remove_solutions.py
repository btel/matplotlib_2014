#!/usr/bin/env python
#coding=utf-8

import sys
import os

def strip(line):
    stripped = line.strip().replace(' ', '')
    return stripped 

def indent(refline, line):
    n_spaces = len(refline) - len(refline.lstrip(' '))
    add_spaces = lambda line: ' ' * n_spaces + line
    return "\n".join(map(add_spaces, line.split('\n')))


if __name__ == "__main__":

    inpath = sys.argv[1]
    outdir = sys.argv[2]

    _, fname = os.path.split(inpath)
    root, ext = os.path.splitext(fname)

    out_fname = fname 
    out_path = os.path.join(outdir, out_fname)
    
    with file(inpath) as fidin, file(out_path, 'w') as fidout:
        line = True
        while line:
            line = fidin.readline()
            if strip(line) == '#SOLUTION':
                refline = line
                while not strip(line)=='#ENDOFSOLUTION':
                    line = fidin.readline()
                line = indent(refline, 
                              '# ENTER YOUR SOLUTION BELOW\n# ...\n')
            fidout.write(line)
