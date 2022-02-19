class person:
    def __init__(self,name,fml):
        self.name = name
        self.family = fml
    @property
    def fullName(self):
        return f'{self.name} {self.family}'
        
        
class user(person):
    def __init__(self,name,family,email):
        #person.__init__(self,name,family)
        #or use super
        super().__init__(name,family)
        self.email = email


poyan = user('mamad','rezoli','mamadjakon@gmail.com')
print(poyan.fullName)