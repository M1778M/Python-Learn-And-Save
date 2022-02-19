import numpy as np

a = np.array([1,2,3,4,1,3])

b = np.array([7,8,9,1,3])

print(np.unique(a)) # Not a tekrari

print()

print(np.union1d(a,b))

print()

print(np.intersect1d(a,b))

print()

print(np.mean(a))

print()

print(np.median(a))

print()

print(np.std(a))

print()

print(np.var(a))

print()

chj = np.array([1,2,2])

print(np.polyval(chj,1))
print(np.polyval(chj,2))

print()

print(np.polyder(chj))

print()

print(np.polyint(chj))

print()