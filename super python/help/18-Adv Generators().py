listA = [x**3 for x in range(10)]

print(listA)

gen1 = (x**3 for x in range(10))
print(gen1)
print(type(listA))
print(type(gen1))
print(listA[2],'\n')
# print(gen1[2])
print(next(gen1))
print(next(gen1))
print(next(gen1))
for i in gen1:
    print(i)



###################################################
gen2 = (x for x in range(10) if x%2 == 0)

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))