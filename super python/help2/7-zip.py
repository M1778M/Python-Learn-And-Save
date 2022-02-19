num = [1,2,3,4]
num_ = [5,6,7,8]
result = zip(num,num_)
print(list(result))
result = zip(num,num_)

print(dict(result))

myl = [(1,2),(3,4),(5,6)]

rs = zip(*myl)

print(list(rs))

st = ['mamad','ali','mamad2']

midterm = [80,89,76]
midterm2 = [90,89,60]
midterm3 = [83,70,76]

#{'mamad' : 90}

#bestn = [max(num for num in zip(midterm,midterm2,midterm3))]
sts = {persons[0]:max(persons[1],persons[2],persons[3]) for persons in zip(st,midterm,midterm2,midterm3)}
print(sts)

stds2 = zip(st,map(lambda pers : max(pers),zip(midterm,midterm2,midterm3)))

print(dict(stds2))