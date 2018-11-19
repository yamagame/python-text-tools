#!/usr/bin/env python3
import sys,os,re,copy
from filter import blackList
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

#argument: N値
#stdin: 形態素解析結果のファイルパス
#stdout: 頻度リスト

N = int(sys.argv[1]) if len(sys.argv) >= 2 else 2

r = re.compile(r'(.+)\t(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+),(.+)')

for line in sys.stdin:
  try:
    p = []
    m = {}
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
          p.append(mo.group(1))
          p = p[-N:]
          q = copy.deepcopy(p)
          #q.sort()
          g = '\t'.join(q)
          if g not in m:
            m[g] = {
              'count': 0,
              'str': g,
            }
          m[g]['count'] += 1
    h = []
    for k in m.keys():
      h.append(m[k])
    h.sort(key=lambda x: x['count'], reverse=True)
    wp,ext = os.path.splitext(line.strip())
    wp = wp+'.'+str(N)+'gram'
    with open(wp, 'w') as fh:
      for k in h:
        fh.write(str(k['str'])+'\t'+str(k['count'])+'\n')
    print(wp)
  except StopIteration:
    print('EOF')
