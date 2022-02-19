print(3+4)
print('3'+'4')

#-----------
class person:
    def __init__(self,name,family,age):
        self.name = name
        self.family = family
        self.age = age
    def __repr__(self): # call return
        return f'{self.name} {self.family}'
    def __len__(self): # len
        return self.age
    def __add__(self,other): # +
        return self.age + other.age
    def __mul__(self): # *
        return self.age * other.age
    def __truediv__(self,other): # /
        return self.age / other.age
    def __sub__(self,other): # -
        return self.age - other.age

per = person('mamad','gholami',29)
per2 = person('reza','gholami zade',34)

print(per)

print(len(per))
print(per + per2)