import numpy as np

n=np.array([[1,2],[3,4]])

print(np.sum(n)) # 1+2+3+4 = 10

print()

print(np.cumsum(n)) # 1 + 2 = 3 / 3 + 3 = 6 / 6 + 4 = 10 -> 1,3,6,10

print()

print(np.cumsum(n,axis=0)) # n[0][0] + n[1][0] = 4 / n[0][1] + n[1][1] = 6 -> [[1,2] , [4,6]]

print()

print(np.cumsum(n,axis=1)) # 1 + 2 = 3 -> n[0][1] / 3 + 4 = 7 -> n[1][1]

print()

print(np.subtract(n,n) ) # [[0,0] , [0,0]]

print()

print(np.divide([5,6,7],3)) # 5 / 3  _|_  6 / 3  _|_  7 / 3  _|

print()

print(np.floor_divide([5,6,7],3)) # خلاصه بالا

print()

print(np.math.sqrt(5)) # جزر عدد

print(np.math.nan) # nan = Not A Number

print(np.math.inf) # بینهایت

print()

this = np.random.uniform(1,5,(2,3)) # from 1 to 5 choose one number -> 2 * 3

print(this)

print()

this_ = np.random.standard_normal((2,1))

print(this_)

print()
