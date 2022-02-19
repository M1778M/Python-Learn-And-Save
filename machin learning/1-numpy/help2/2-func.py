import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

arr_ = np.arange(0,16,3).reshape(1,6)

print(arr_,'\n',arr_.size,'\n',arr_.dtype)


print(arr_.itemsize)



arr6 = np.linspace(1,5,num=10,dtype=int,endpoint=True) # start , stop, num
print(arr6)


arr7 = np.logspace(0,5,num=5,dtype=int)
print(arr7)


arr8=np.geomspace(1,5,num=10)
print(arr8)