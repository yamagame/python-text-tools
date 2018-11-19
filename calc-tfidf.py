#!/usr/bin/env python3
import sys,os,re
from math import log
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

freqData = sys.argv[1] if len(sys.argv) >= 2 else '/tmp/frequency.gfrq'

re_f = re.compile(r'(.+)\t(.+)\t(.+)\t(.+)')
freq = {}

try:
  with open(freqData, 'r') as fp:
    for cnt, l in enumerate(fp):
      mo = re_f.search(l)
      if mo != None:
        freq[mo.group(1)] = {
          'count': int(mo.group(2)),
          'df': float(mo.group(3)),
          'type': mo.group(4),
        }
except OSError:
    print('EOF')

re_r = re.compile(r'(.+)\t(.+)\t(.+)\t(.+)')

for line in sys.stdin:
  try:
    wp,ext = os.path.splitext(line.strip())
    wp = wp+'.tfidf'
    h = []
    with open(line.strip(),'r') as fp:
      for cnt, l in enumerate(fp):
        mo = re_r.search(l)
        if mo != None:
          w = freq[mo.group(1)]
          idf = log(w['df'])+1
          h.append({
            'str': mo.group(1),
            'count': mo.group(2),
            'tf': mo.group(3),
            'idf': idf,
            'tfidf': float(mo.group(3))*idf,
            'type': mo.group(4),
          })
    h.sort(key=lambda x: x['tfidf'], reverse=True)
    with open(wp, 'w') as fh:
      for k in h:
        fh.write(str(k['str'])+'\t'+str(k['count'])+'\t'+str(k['tf'])+'\t'+str(k['idf'])+'\t'+str(k['tfidf'])+'\t'+str(k['type'])+'\n')
    print(wp)
  except StopIteration:
    print('EOF')
