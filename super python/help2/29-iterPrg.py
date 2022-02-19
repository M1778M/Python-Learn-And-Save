class user:
    active_u = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Usr_dict={'name' : name,'age':age}
        user.active_u.append(Usr_dict)
    def logout(self):
        print(f'{self.name} is logouted')
        cuser = list(filter(lambda user:user['name']==self.name,
        user.active_u))[0]
        print(cuser)



me = user('mamad',29)
you = user('nazi',25)
me.logout()
print(user.active_u)
