import numpy as np

r = np.arange(1,10,3) # range(1,10,3) but To array

a = np.array([[1,2],[3,4]])

print(r)

print()

v = np.linspace(1,10,5) # start , end , how much number to create

print(v)

print()

mymask = a>2

print(mymask)

print()

mymask2 = np.logical_and(a>1,a<4)

print(mymask2)

print()

print(np.ones((1,3))) # create 1 * 3 array and set 1

print()

print(np.zeros((2,3))) # create 2 * 3 array and set 0

print()

print(np.size(a))

print()

print(np.shape(a))
