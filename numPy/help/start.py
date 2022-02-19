#!
import numpy as np

mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(mat)
print()
vl = np.array([1,2,3,4,5,6,7,8,9])

print(vl)

print()
ar = np.arange(1,100,3)

print(ar)


ls = np.linspace(0,10,50)

print()
print(ls)
print(ls.shape)


test_mat = np.array([[1,5,2],
                    [55,22,33],
                    [65,4,-2]])
print()
print(np.max(test_mat))
print(np.min(test_mat))
print(np.sum(test_mat))
