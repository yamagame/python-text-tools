#!/usr/bin/env python3
import sys,os,re
import math

KEY = sys.argv[1].strip() if len(sys.argv) >= 2 else ''

separator = '\t'

data = [
  [],
  [],
]
l = 0
T = None

for line in sys.stdin:
  if KEY == '':
    print(line)
  else:
    p = [ x.strip() for x in line.split(separator) ]
    if len(p) <= 1:
      l = 1 if l == 0 else l
    else:
      if p[0] == KEY:
        T = p
      data[l].append(p)

def Sort(data, T):
  r = []
  for i,v in enumerate(data):
    dx = float(v[1])-float(T[1])
    dy = float(v[2])-float(T[2])
    l = dx*dx+dy*dy
    q = {
      'v': v,
      'l': l,
    }
    r.append(q)
  r.sort(key=lambda x: x['l'])
  return r

def PrintData(data):
  for i,v in enumerate(data):
    w = v['v']
    print("{}\t{}\t{}".format(w[0],w[1],w[2]))

PrintData(Sort(data[0], T))

print(' ')

PrintData(Sort(data[1], T))
