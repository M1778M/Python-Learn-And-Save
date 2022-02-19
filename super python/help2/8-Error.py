#print(test)

#raise SyntaxError ('Not Need')


def fullname(fname,lname):
    if type(fname) is not str or type(lname) is not str:
        raise TypeError(f'{fname} or {lname} is not str')
    return f"{fname} {lname}"
    
#print(fullname('mamad',3))

