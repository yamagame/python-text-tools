#!/usr/bin/env python
import sys,os,errno
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

#Usage: ./readdir.py [拡張子] [探索ディレクトリ]
#argument: 探索ディレクトリ
#stdout: 拡張子が.xmlのファイルパス

#find . -name '*.xml' と同じ

path = sys.argv[2] if len(sys.argv) >= 3 else '.'
ext  = sys.argv[1] if len(sys.argv) >= 2 else 'xml'

for foldername, subfolders, filenames in os.walk(path):
  for filename in filenames:
    p = os.path.join(foldername, filename)
    r, e = os.path.splitext(p)
    if e=='.'+ext:
      print(os.path.join(foldername, filename))
