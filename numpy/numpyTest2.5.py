# coding=utf-8
import numpy as np

A = np.arange(3, 15).reshape((3, 4))

print A
print A[2]
print A[:,2]
# 第2列所有数字
print A[1,1:3]
# 第一行1到3位之间的数字

for row in A:
    print row
# 迭代每一行,可以通过迭代A的转置矩阵来迭代A和列
print '----------------------'

for item in A.flat:
    print item
