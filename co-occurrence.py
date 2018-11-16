#!/usr/bin/env python
import sys,os,re
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

N = int(sys.argv[1]) if len(sys.argv) >= 2 else 2

re_r = re.compile(r'(.+?)\t(.+)')
re_q = re.compile(r'(.+)\((.+)\)')

wordhash = {}
docarray = []

for line in sys.stdin:
  mo = re_r.search(line)
  if mo != None:
    doc = {
      'fname': mo.group(1),
      'words': {},
    }
    words = mo.group(2).split('\t')
    for i,t in enumerate(words):
      po = re_q.search(t)
      if po != None:
        v = po.group(1)
        doc['words'][v] = True;
        if v not in wordhash:
          wordhash[v] = 1
        else:
          wordhash[v] += 1
      else:
        v = t
        doc['words'][v] = True;
        if v not in wordhash:
          wordhash[v] = 1
        else:
          wordhash[v] += 1
    docarray.append(doc)

wordarray = []
for k in wordhash.keys():
  wordarray.append({ 'word': k, 'count':  wordhash[k] })

wordarray.sort(key=lambda x: x['count'], reverse=True)

temphash = {}
for i,v in enumerate(wordarray):
  for j,w in enumerate(wordarray):
    if j>i:
      vs = v['word']
      ws = w['word']
      for k,d in enumerate(docarray):
        words = d['words']
        if (vs in words) and (ws in words):
          key = vs+'\t'+ws
          if key not in temphash:
            temphash[key] = 0
          temphash[key] += 1

result = []
for k in temphash.keys():
  result.append({
    'key': k,
    'count': temphash[k],
  })

result.sort(key=lambda x: x['count'], reverse=True)

for i,v in enumerate(result):
  if v['count'] >= N:
    print(v['key']+'\t'+str(v['count']))
