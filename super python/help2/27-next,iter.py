#iterable
#iterator
numbers = [1,2,3,4,5]

#for i in numbers:
#    print(i)
    

def for_i_in_(iterable,func):
    iterator =iter(iterable)
    while(True):
        try:
            i = next(iterator)
        except:
            break
        else:
            func(i)


iternums = iter(numbers)

#print(next(iternums))
#print(next(iternums))
#print(next(iternums))
#print(next(iternums))
#print(next(iternums))

for_i_in_(numbers,print)

