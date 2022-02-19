#_name
#__name
#__name__

class user:
    def __init__(self,name,email,password):
        self.username = name
        self._email = email
        self._password = password
        self.__id = 23
    def login(self,getpass):
        if getpass == self._password:
            print('login!')
        else:
            print('wrong password')
    


me = user('Mamad','test@gmail.com',12345)
print('username : ' + me.username + ' email : ' + me._email + ' password : ' + str(me._password) + ' id : ' + str(me._user__id) )
me.login(12345)