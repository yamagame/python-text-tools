#!/usr/bin/env python
import sys,os,re
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

N = int(sys.argv[1]) if len(sys.argv) >= 2 else 30
W = sys.argv[2] if len(sys.argv) >= 3 else None

for line in sys.stdin:
  try:
    fname = line.strip()
    o = fname
    f = False
    with open(fname,'r') as fp:
      for cnt, l in enumerate(fp):
        if cnt > N: break
        mo = l.split('\t')
        if len(mo) > 0:
          mo = mo[:-1]
          #mo.sort()
          c = '\t' if o != '' else ''
          o = o + c + '/'.join(mo)
          if W == None or mo.group(1) == W:
            f = True
    if f: print(o)
  except StopIteration:
    print('EOF')
