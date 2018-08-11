# coding=utf-8
import numpy as np
import pandas as pd

# 处理丢失数据
dates = pd.date_range('20180719', periods=6)
print dates
print '------------------------------------------------'

df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df.iloc[2, 2] = np.nan
df.iloc[0, 1] = np.nan
df.iloc[3, 2] = np.nan

print '删除所有有空数据的条目 默认按行删除---------------------------------------------'
print df.dropna()

print '删除所有有空数据的条目 1是列，0是行 此处是1 ---------------------------------------------'
print df.dropna(axis=1)

print '删除所有有空数据的条目 1是列，0是行 how=all  默认是any all的话一个叶不丢掉---------------------------------------------'
print df.dropna(axis=0, how='all')

print 'Nan填充为0-----------------------------------------------'
print df.fillna(value=0)

print "数据中书否有空数据"
print np.any(df.isnull())