num = [1,2,5,7,4,6,8,4]
print(num)
#num.sort()
numSort = sorted(num)
print(numSort)
numSort = sorted(num,reverse=True)
print(numSort)

users=[{'name': 'mamad','age' : 23},
       {'name': 'mamad2','age' : 22},
       {'name': 'mamad3','age' : 24},
       {'name': 'mamad4','age' : 53},
       {'name': 'mamad5','age' : 43},
       {'name': 'mamad6','age' : 33},
       {'name': 'mamad7','age' : 23}]

print(sorted(users,key=lambda user:user['age'] ))
print()
#-------------------------------------
chars = ['a','z','t']
name = "HELLO MAN Yooooz"
print(max(num))
print(min(num))
print('-----------------------')
print(max(chars))
print(min(chars))
print('----------------------')
print(max(name))
print(min(name))

names = ['mamad','sara','reza','gholamreza']

print([len(nam) for nam in names])
print(max(names,key=lambda n:len(n)))