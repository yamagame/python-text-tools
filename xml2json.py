#!/usr/bin/env python3
import sys,os
import xml.etree.ElementTree as ET
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

for line in sys.stdin:
  try:
    file = open(line.strip(),'r',-1,'euc_jp')
    content = file.read()
    root = ET.fromstring(content)

    def parse(r, tag, c, p):
      if r.tag == tag:
        p=True
      if p:
        if r.text != None and r.text!='' and r.text!='\n':
          c += r.text.strip()
      for child in r:
        if child.tag == 'br':
          if p:
            c += '\n'
          c += parse(child, tag, '', p)
        else:
          c += parse(child, tag, '', p)
      if p:
        if r.tail != None and r.tail!='' and r.tail!='\n':
          c += r.tail.strip()
      if r.tag == tag:
        p=False
        c+='\n'
      return c

    value = {}

    def doParse(tag):
      value[tag] = parse(root, tag, '', False,)

    doParse('tech-problem')
    doParse('background-art')
    doParse('technical-field')
    doParse('tech-solution')
    doParse('description-of-drawings')
    doParse('description-of-embodiments')
    doParse('reference-signs-list')
    doParse('claim-text')

    text = json.dumps(value, ensure_ascii=False, indent=2)

    wp,ext = os.path.splitext(line.strip())
    wp = wp+'.json'
    with open(wp, 'w') as fh:
      fh.write(text)
    
    print(wp)

    file.close()
  except StopIteration:
    print('EOF')
