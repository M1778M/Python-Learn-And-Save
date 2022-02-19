import numpy as np

arr = np.zeros((3,4),dtype=int) # 3 * 4
print(arr)


arr2 = np.zeros(12,dtype=int)
print(arr2)


arr3 = np.ones((3,4),dtype=int) # 3 * 4
print(arr3)


arr4 = np.empty(4)
print(arr4)


arr5 = np.random.default_rng(1)
arr5 = arr5.random(6)
print(arr5)
