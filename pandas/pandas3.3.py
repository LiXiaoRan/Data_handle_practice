# coding=utf-8
import numpy as np
import pandas as pd

dates = pd.date_range('20180719', periods=6)
print dates
print '------------------------------------------------'

df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print '修改2行2列值-----------------------------------------------'
df.iloc[2, 2] = 1111
df.loc['20180719', 'a'] = 500
df.c[df.c > 1110] = 1211
# 只修改c列大于1110的数字，不会影响一行
df['F'] = np.nan
# 增加F列
df['E'] = pd.Series(np.arange(1, 7), index=pd.date_range('20180719', periods=6))
print df
