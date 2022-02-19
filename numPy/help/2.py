import numpy as np

#command
"""
NumPy/

np.shape
np.reshape
np.size
np.dtype
np.itemsize
np.where
np.zeros
np.ones
"""
mat = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
#shape
print(mat.shape)
np.shape(mat)
#reshape
print(mat.reshape(3,5))
#size , dtype , itemsize
print(mat.size)
print(mat.dtype)
print(mat.itemsize)
#where
#np.where(shart, True,False)
print()
sm = np.array([[10,-10,424],
               [525,-24,1341],
               [13,-141,-1431]])

print(np.sum(sm > 0))
print()
print(np.where(sm > 0,1,0))
print('\n')
#zeros
o = np.zeros((150,130))
print(o)
print('\n')
#ones
one = np.ones((300,100))
print(one)
