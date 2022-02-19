def count_up_to(max):
    count = 1
    while (count<max):
        yield count
        count+=1
        
        
        
counter = count_up_to(10)

#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))
#print(next(counter))

#----------------------------------------
# |1|2|3|4|5|6|7| 8
# |1|1|2|3|5|8|13|21|

def fib(max):
    nums=[]
    a,b=0,1
    while(len(nums)<max):
        nums.append(b)
        a,b=b,a+b
    return nums
    
print(fib(10))

