import numpy as np

array = np.array([[1, 22, 3]
                     , [2, 32, 4]
                  ], dtype=np.int64)
print (array)
print 'dtype is ', array.dtype
print 'number of dim:', array.ndim
print 'shape: ', array.shape
print 'size', array.size

a = np.zeros((3, 4), dtype=int)
print a

b = np.ones((3, 4), dtype=float)
print b

c = np.arange(12).reshape((3, 4))
print c

d = np.linspace(1, 10, 21).reshape((3, 7))
print d
