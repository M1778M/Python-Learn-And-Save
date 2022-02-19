class IUserService:
    def GetAllUsers(self):
        raise NotImplementedError
    def GetUserById(self): raise NotImplementedError
    def CreateNewUser(self): raise NotImplementedError


class UserServicesBySql(IUserService):
    def CreateNewUser(self):
        print('new user created')
    def GetAllUsers(self):
        print('all user is ready')
    def GetUserById(self):
        print('all users have an id')


class UserServicesByOracle(IUserService):
    def CreateNewUser(self):
        print('new user created')
    def GetAllUsers(self):
        print('all user is ready')
    def GetUserById(self):
        print('all users have an id')


user1 = UserServicesBySql()
user1.CreateNewUser()
user1.GetUserById()
#-----------------------------------

print(5+4)
print('5'+'4')

#--------------------------------
class car:
    def move(self):
        raise NotImplementedError



class benz(car):
    def __init__(self,mdl):
        self.mdl = mdl
        
    def move(self):
        print(f'{self.mdl} is moving')


class bmw(car):
    def __init__(self,mdl):
        self.mdl = mdl
    def move(self):
        print(f'{self.mdl} is moving')


cls=benz('cls')
x4=bmw('x4')

cls.move()

x4.move()

class peraid(car):
    def __init__(self,mdl):
        self.mdl = mdl
    def move(self):
        print(f'{self.mdl} is moving')


peride111=peraid('111')
peride111.move()

#----------------------------------------------



#numbers= [1,2,3,4,5,6]
#mynum = {1,2,3,4,5,6}
#
#mydict = {'name':'mamad','family':'rezaii'}
#
#numbers.copy()
#
#mynum.copy()
#
#mydict.copy()
#
#len(numbers)
#len(mynum)
#len(mydict)
