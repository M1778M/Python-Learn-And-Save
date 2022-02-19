class user:
    def __init__(self,name,fml,age):
        self.username = name 
        self.family = fml
        self.age = age
        self.syn = f'{self.username} {self.family} {self.age} , '
    def __repr__(self):
        return f'{self.username} {self.family} is {self.age}'
    def __add__(self,other):
        return self.syn + self.syn.rstrip(' , ')
    def __sub__(self,other):
        return self.age - other.age
    
me = user('poyan','mamadi',23)

print(me)

you = user('ali','mamadi',39)

print(you)
print(me+you)
print(me-you)