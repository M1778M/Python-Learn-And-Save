print(all([1,2,3,4,5,6,0])) # 0 = Faslse
all([1,2,3,4]) # True

num = [2,4,6]

print(all([x%2==0 for x in num]))

print(any([True,True,True,False])) # True
print(any([False])) # False

print(any([]))
print(all([]))

print(any[x%2==0 for x in num])

users = [{'name' :'poyan','shop' : ['pen']},{'name' : 'reza','shop' : [] },{'name' : 'ali','shop' : ['pen','book']}]


rs = all([len(users['shop']) == 0 for user in users])

print(rs)

