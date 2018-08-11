import numpy as np

array = np.random.random((2, 4))

print array
print np.sum(array, axis=1)
# axis=1是对行求和，0是对列求和
print np.min(array)
print np.max(array)
