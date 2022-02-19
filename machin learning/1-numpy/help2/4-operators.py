import numpy as np


a = np.arange(1,5,dtype=int)
b = np.arange(5,9,dtype=int)
print(a)

print(b)

print(a+b) # element + element -> return 1element


print(a*b) # element * element -> return 1element

print(a@b) # sum * b


print(a.dot(b)) # sum * b

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
print(a,'\n\n\n',b)

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(3,2)
print(a@b)


print(a.sum(axis=1))

print(a.cumsum(axis=1))