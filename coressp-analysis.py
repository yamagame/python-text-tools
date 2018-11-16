#!/usr/bin/env python
import sys,os,re
import numpy as np
import numpy.random as random
import mca, pandas

csvFile = sys.argv[1] if len(sys.argv) >= 2 else ''
separator = '\t'

def DataFrame(csvFile):
  if csvFile == '':
    body = []
    for line in sys.stdin:
      body.append([ x.strip() for x in line.split(separator) ])
    data = pandas.DataFrame(body)
    col = data.loc[0:0,1:].values[0]
    row = [ os.path.basename(x) for x in np.array(data.loc[:,0:0].values[1:]).flatten() ]
    bod = data.loc[1:,1:].astype(float).values
    adata = pandas.DataFrame(data=bod, index=row, columns=col)
    return adata
  else:
    adata = pandas.read_table(csvFile, skiprows=0, index_col=0, sep=separator)
    print(adata)
    return adata

df = DataFrame(csvFile)

mca_ben = mca.MCA(df, ncols=df.shape[1], benzecri=False)

result_row = pandas.DataFrame(mca_ben.fs_r(N=2))
result_row.index = list(df.index)

result_row.to_csv(sys.stdout, sep='\t', encoding='utf-8', header=False)

result_col = pandas.DataFrame(mca_ben.fs_c(N=2))
result_col.index = list(df.columns)

result_col.to_csv(sys.stdout, sep='\t', encoding='utf-8', header=False)
