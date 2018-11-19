#!/usr/bin/env python3
import sys,os,re
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

N = int(sys.argv[1]) if len(sys.argv) >= 2 else 2

re_r = re.compile(r'(.+?)\t(.+)')
re_q = re.compile(r'(.+)\((.+)\)')
re_s = re.compile(r'(.+),(.+)')

wordhash = {}
wordarray = []
docarray = []

def appendWord(v):
  if v not in wordhash:
    wordhash[v] = {
      'word': v,
      'count': 1,
      'index': len(wordarray),
    }
    wordarray.append(wordhash[v])
  else:
    wordhash[v]['count'] += 1

for line in sys.stdin:
  mo = re_r.search(line)
  if mo != None:
    doc = {}
    words = mo.group(2).split('\t')
    for i,t in enumerate(words):
      po = re_q.search(t)
      if po != None:
        v = po.group(1)
        w = re_s.search(po.group(2))
        if w != None:
          appendWord(v)
          doc[v] = {
            'count': w.group(1),
            'info': wordhash[v],
          }
      else:
        v = t
        appendWord(v)
        doc[v] = {
          'count': '1',
          'info': wordhash[v],
        }

    docarray.append({
      'fname': mo[1],
      'doc': doc,
    })

wordarray.sort(key=lambda x: x['count'], reverse=True)
wordarray = [x for x in wordarray if x['count'] >= N]

header = ''
for i,v in enumerate(wordarray):
  header += '\t'
  header += v['word']
  #header += v['word']+':'+str(v['count'])

print(header)

for i,v in enumerate(docarray):
  line = ''
  for j,w in enumerate(wordarray):
    line += '\t'
    if w['word'] in v['doc']:
      line += v['doc'][w['word']]['count']
    else:
      line += '0'
  print(v['fname']+line)
