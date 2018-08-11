# coding=utf-8
import numpy as np

A = np.array([1, 1, 1])[:, np.newaxis]  # 增加向量 这样后边用讲A和B变成列来合并，也可以用reshape
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack
# 上下合并A和B
print '上下合并'
print C

D = np.hstack((A, B))
# 左右合并
print '左右合并'
print D

print 'A和C的shape'
print A.shape, C.shape

print A.T
# 这种方式不能把一个行变成一个列

# 增加向量
# print A[:, np.newaxis].T


E = np.concatenate((A, B, B, A),axis=1)
# 合并多个array 1是横向合并 0是纵向合并
print E
