# coding=utf-8
import numpy as np
import pandas as pd

# 合并 concat

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

print df1
print df2
print df3

print '上下合并 concat------------------------------------------------'

res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # ignore_index=True重新排列索引
print res

print '合并 join------------------------------------------------'

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

print df1
print df2

res = pd.concat([df1, df2], axis=0, join='outer', ignore_index=True)
print res
# outer直接合并 并集
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
print res
# 裁剪合并 交集

print 'join_axes ------------------------------------------------'

res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print res

print 'append ------------------------------------------------'

res = df1.append([df2, df3], ignore_index=True)
print res
