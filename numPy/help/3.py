import numpy as np

"""NumPy - random
np.random.rand()
np.random.random()
np.random.randint()
np.random.shuffle()
np.random.normal()
np.random.normal(size=())
np.random.uniform()
np.random.uniform(size=())
np.random.choise([])
np.random.choise([],size=())
"""

#rand
print(np.random.rand(5))
print()
print(np.random.rand(5,2))
#random
print()
mat = np.random.random((3,4))
print(mat)
print()
#randint
print(np.random.randint(0,100,8))
print()
print(np.random.randint(0,11,6).reshape(3,2))
print()
#shuffle
mat = np.arange(1,50).reshape(7,7)
print(mat)
print()
np.random.shuffle(mat)
print(mat)
print()
#normal
print(np.random.normal())
print(np.random.normal(5))
print()
#uniform
print(np.random.uniform())
print()
print(np.random.uniform(size=10))
print()
#choise
mylist = [3,-6,7,5,2,-5,3,1]

print(np.random.choice(mylist))
print()
print(np.random.choice(mylist,size=3))
print()
print(np.random.choice(mylist,size=(2,4)))
