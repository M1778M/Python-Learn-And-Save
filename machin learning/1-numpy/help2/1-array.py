import numpy as np

arr = np.array([1,2,3,4])
print(arr)

print(arr[2])


arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)


print(arr2[0,2])


arr3=np.array([[1,2,3,4],[5,6,7,8],[9,10,11]])

print(arr3)


arr4=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr4)


from1to3 = arr[0:3:1] # from , to , step example range()
print(from1to3)


arr5 = np.array([1,2,3,4,5,6,7,8,9,10])
this = arr5[2:8:3]

print(this)

c = arr4[1:3,1:3]
print(c)
