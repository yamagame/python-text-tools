#!/usr/bin/env python3
import sys,os
import subprocess
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

#stdin: JSONファイル(UTF8)
#stdout: 形態素解析結果

for line in sys.stdin:
  try:
    file = open(line.strip(),'r')
    content = file.read()
    file.close()
    
    root = json.loads(content)

    wp,ext = os.path.splitext(line.strip())
    wp = wp+'.mecab'
    fh = open(wp, 'w')

    def doMecab(key):
      techSolution = root[key]
      for line in techSolution.split('。'):
        if line.strip() != '':
          #print(':'+line.strip())
          ps = subprocess.Popen(('echo', line.strip()+'。'), stdout=subprocess.PIPE)
          output = subprocess.check_output(['/usr/bin/env', 'mecab', '-b', '32768'], stdin=ps.stdout)
          #print(':'+output.decode('utf8'))
          fh.write(output.decode('utf8')+'\n')
          ps.wait()

    doMecab('tech-problem')
    doMecab('background-art')
    doMecab('technical-field')
    doMecab('tech-solution')
    doMecab('description-of-drawings')
    doMecab('description-of-embodiments')
    doMecab('reference-signs-list')
    doMecab('claim-text')

    fh.close()

    print(wp)

  except StopIteration:
    print('EOF')
