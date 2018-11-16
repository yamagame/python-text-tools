#!/usr/bin/env python
import sys,os,re
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

N = int(sys.argv[1]) if len(sys.argv) >= 2 else 30
W = sys.argv[2] if len(sys.argv) >= 3 else None
re_r = re.compile(r'(.+)\t(.+)\t(.+)\t(.+)\t(.+)\t(.+)')

for line in sys.stdin:
  try:
    fname = line.strip()
    o = fname
    f = False
    with open(fname,'r') as fp:
      for cnt, l in enumerate(fp):
        if cnt > N: break
        mo = re_r.search(l)
        if mo != None:
          c = '\t' if o != '' else ''
          o = o + c + mo.group(1) + '(' + mo.group(2) + ',' + mo.group(5) + ')'
          if W == None or mo.group(1) == W:
            f = True
    if f: print(o)
  except StopIteration:
    print('EOF')
