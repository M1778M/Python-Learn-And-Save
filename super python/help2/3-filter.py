num=[1,2,3,4,5,6]

evens=filter(lambda x:x%2==0,num)

print(list(evens))

users = [{'name' : 'ali','skill':['python','csharp']},{'name' : 'masih','skill' : ['kotlin','ZeroMine']},{'name' : 'mamad','skill' : []}]


result = filter(lambda user:not user['skill'],users)

result2 = map(lambda user:user['name'],result)

#print(list(result))
print(list(result2))

