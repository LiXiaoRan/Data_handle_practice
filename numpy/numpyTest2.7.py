# coding=utf-8
import numpy as np

A = np.arange(12).reshape((3,4))
print A

print np.split(A,2,axis=1)
# 对列进行操作分成两块

print np.split(A,3,axis=0)
# 对行进行操作分成三块，目前split只能使用均等分割

print '--------------------'
print np.array_split(A,3,axis=1)
# 不等分割

print '--------------------'
print np.vsplit(A,3)
print np.hsplit(A,2)