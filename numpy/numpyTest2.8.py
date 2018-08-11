# coding=utf-8
import numpy as np

a = np.arange(4)
b = a
c = a
d = b
a[0] = 11

print b is a
print b

print d is a
print d

d[1:3] = [22, 33]
print a

# a b c d都是指向a，改变任意一个其他的全变。

print '--------------------'

b = a.copy()
# 使用copy可以杜绝这种情况
print b is a
