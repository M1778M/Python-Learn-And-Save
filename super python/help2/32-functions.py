from random import choice

def sumTo(num,func):
    total = 0
    for n in range(0,num+1):
        total += func(n)
    return total

def squer(x):
    return x*x

print(sumTo(5,squer))



#------------------

def greet(per):
    def get_mod():
        msg = choice(('Hello ','Hi ','GoodMorning ','Bye '))
        return msg

    result = get_mod() + per
    return result
    
print(greet('Ali'))
