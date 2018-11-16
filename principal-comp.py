#!/usr/bin/env python
import numpy as np
import numpy.random as random

random.seed(0)
A = (random.randn(16)*10).reshape(8,2)
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

for i,v in enumerate(A):
  print(str(i)+'\t'+str(v[0])+'\t'+str(v[1]))

print('')

for i,v in enumerate(T):
  print(str(i)+'\t'+str(v[0])+'\t'+str(v[1]))
