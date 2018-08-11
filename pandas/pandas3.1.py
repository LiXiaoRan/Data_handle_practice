# coding=utf-8
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print s

dates = pd.date_range('20180719', periods=6)
print dates
print '------------------------------------------------'

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print df

print '------------------------------------------------'

df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
print df2

print '计算每一列的各种数据'
print df2.describe()

print '------------------------------------------------'

print df.sort_index(axis=1, ascending=False)
# 按行索引排序 倒叙
