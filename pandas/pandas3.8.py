# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 累加
# data.plot()
# plt.show()


data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
# print data
data = data.cumsum()  # 累加
# data.plot()
# plt.show()

# plot method: bar hist box kde area scatter hexbin pie
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2',ax=ax)
plt.show()

