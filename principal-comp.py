#!/usr/bin/env python3
import sys,os,re
import numpy as np
import numpy.random as random
import pandas

csvFile = sys.argv[1] if len(sys.argv) >= 2 else ''
separator = '\t'

def DataFrame(csvFile):
  if csvFile == '':
    body = []
    for line in sys.stdin:
      body.append([ x.strip() for x in line.split(separator) ])
    data = pandas.DataFrame(body)
    #col = data.loc[0:0,1:].values[0]
    row = [ os.path.basename(x) for x in np.array(data.loc[:,0:0].values[0:]).flatten() ]
    bod = data.loc[0:,1:].astype(float).values
    adata = pandas.DataFrame(data=bod, index=row)
    return adata
  else:
    adata = pandas.read_table(csvFile, index_col=0, header=None, sep=separator)
    del adata.index.name
    return adata

df = DataFrame(csvFile)
#print(df.values)

def comp(A):
  #random.seed(0)
  #A = (random.randn(16)*10).reshape(8,2)

  A = A-A.mean(axis=0)
  CONV = np.cov(A, rowvar=False)
  l,v = np.linalg.eig(CONV)
  l_index = np.argsort(l)[::-1]
  l_ = l[l_index]
  v_ = v[:,l_index]
  comp = v_[:,:2].T
  T = (np.mat(A)*(np.mat(comp.T))).A*np.array([1, -1])
  # print(A)
  # print(T)
  # print(l_)
  # print(v_)

  # for i,v in enumerate(A):
  #   print(str(i)+'\t'+str(v[0])+'\t'+str(v[1]))

  # print('')

  for i,v in enumerate(T):
    print(str(i)+'\t'+str(v[0])+'\t'+str(v[1]))

comp(df.values)
