class user:
    AgeError = 'Age Is Not True'
    def __init__(self,name,age):
        self.name = name
        if age>0:
            self._age = age
        else:
            self._age = self.AgeError
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value>0:
            self._age = value
    @property
    def full_name(self):
        return f'{self.name} is {self.age}'
    
    
    def get_age(self):
        return self._age
    def set_age(self,value):
        if value>0:
            self._age = value
        else:
            self._age = self.AgeError
            


me = user('mamad',39)
print(me.age)
me.age = 12
print(me.age)

print(me.full_name)
