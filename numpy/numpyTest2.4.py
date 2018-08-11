# coding=utf-8
import numpy as np

A = np.arange(2, 14).reshape((3, 4))

print A
print np.argmin(A)
# 最小值索引
print np.argmax(A)
# 最大值索引
print np.mean(A)
# 最平均值
print np.cumsum(A)
# 元素累加
print np.median(A)
# 中位数
print np.diff(A)
# 累差
print np.sort(A)

print A.T
# 转置

print np.clip(A,5,9)
# 大于9的全变成9 小于5的全变成5，其余不变

