"""numbers = [1,2,3,4,5]
doubles=[]
for i in numbers:
    doubles.append(i*2)

print(doubles)
"""
numbers = [1,2,3,4,5]

doubles=map(lambda num:num*2,numbers)

print(list(doubles))
print(doubles)
print(list(doubles))


names=["ali",'reza','mamad','mamad jakon']

upername = map(lambda name:name.upper(),names )

print(list(upername))

people = [{'name' : 'mamad','family' : 'jakon','age' : 39}]

fm = map(lambda pl:pl['family'],people)

print(list(fm))

