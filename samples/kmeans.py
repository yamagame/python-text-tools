import numpy as np
import sklearn

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#sklearnに入ってるmake_blobsを使用
X,y = make_blobs(random_state=10)
#X = [[0,0], [10,10], [30,30]]

kmeans = KMeans(init='random',n_clusters=3)
kmeans.fit(X)

y_pre = kmeans.fit_predict(X)

r=[[],[],[]]

for i,v in enumerate(X):
  r[y_pre[i]].append(v)

for i,x in enumerate(r):
  for j,v in enumerate(x):
    print(str(i)+'-'+str(j)+'\t'+str(v[0])+'\t'+str(v[1]))
  print('')
