class person:
    def __init__(self,name):
        print('in person')
        self.name = name
    def sayH(self):
        return f'Hello {self.name} in person'
    def sayB(self):
        return f'goodbye {self.name}'
        

class user:
    def __init__(self,name):
        print('in user')
        self.name = name
    def sayH(self):
        return f'Hello {self.name} in user'
    def sayOK(self):
        return f'Ok {self.name}'
        

class admin(person,user): #TODO Person is number 1 to use
    def __init__(self,name):
        print('in admin')
        super().__init__(name)
        user.__init__(self,name)
        person.__init__(self,name)
        
        
        

per1 = admin('mamad')
print(per1.sayH())
print(per1.sayB())
print(per1.sayOK())

print(isinstance(per1,admin))
print(isinstance(per1,user))
print(isinstance(per1,person))

#method resoluthion order
#__mro__
#mro()
#help(className)
#-------mro
#print(help(admin))
#print(admin.__mro__)
#print(admin.mro())

class a: # yoo man i have use me
    def sh(self):
        print('Hello in a')

class b(a): # Ineed Check c
    #def sh(self):
    #   print('Hello in b')
    pass
class c(a): # Ineed Too But I using a check a 
    #def sh(self):
    #    print('Hello in c')
    pass
class d(b,c): #> NotHave GoTo b
    #def sh(self):
    #    print('Hello in d')
    pass
x = d()
x.sh()
print(d.mro())

