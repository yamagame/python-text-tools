#!/usr/bin/env python3
import sys,os,re
from filter import blackList
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

#stdin: 形態素解析結果のファイルパス
#stdout: 頻度リスト

freqData = sys.argv[1] if len(sys.argv) >= 2 else '/tmp/frequency.gfrq'
T = 1

r = re.compile(r'(.+)\t(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+)')

totalword = {}
totalpaper = 0

for line in sys.stdin:
  try:
    m = {}
    total = 0
    with open(line.strip(),'r') as fp:
      for cnt, l in enumerate(fp):
        mo = r.search(l)
        if mo != None:
          word = mo.group(1)
          if blackList(word, mo): continue
          if mo.group(2) == '記号': continue
          if mo.group(2) == '名詞' and mo.group(1) == '．': continue
          if mo.group(2) == '名詞' and mo.group(3) == '数': continue
          if mo.group(2) == '助詞': continue
          if mo.group(1) not in m:
            m[mo.group(1)] = {
              'count': 0,
              'type': mo.group(2),
              'raw': mo,
              'str': mo.group(1),
            }
          m[mo.group(1)]['count'] += 1
          if m[mo.group(1)]['count'] == T:
            if mo.group(1) not in totalword:
              totalword[mo.group(1)] = {
                'count': 0,
                'type': mo.group(2),
                'str': mo.group(1),
              }
            totalword[mo.group(1)]['count'] += 1
          total += 1
    h = []
    for k in m.keys():
      m[k]['tf'] = m[k]['count']/total
      h.append(m[k])
    h.sort(key=lambda x: x['tf'], reverse=True)
    wp,ext = os.path.splitext(line.strip())
    wp = wp+'.freq'
    with open(wp, 'w') as fh:
      for k in h:
        fh.write(str(k['str'])+'\t'+str(k['count'])+'\t'+str(k['tf'])+'\t'+str(k['type'])+'\n')
    print(wp)
    totalpaper += 1
  except StopIteration:
    print('EOF')

with open(freqData, 'w') as fh:
  h = []
  for k in totalword.keys():
    totalword[k]['df'] = totalpaper/totalword[k]['count']
    h.append(totalword[k])
  h.sort(key=lambda x: x['df'], reverse=True)
  for k in h:
    fh.write(str(k['str'])+'\t'+str(k['count'])+'\t'+str(k['df'])+'\t'+str(k['type'])+'\n')
