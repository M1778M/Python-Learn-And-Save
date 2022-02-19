class user:
    userc = 0
    allowuser = ['poyan','mamad','sara','nazi']
    cruser = []
    def __init__(self,name,fml):
        if name not in user.allowuser:
            raise ValueError(f'{name} is not Allowed To Create')
        self.username = name
        self.family = fml
        user.userc += 1
        user.cruser.append(name)
    def delete(self):
        print(f"{self.username} is delete")
        user.userc-=1
        user.cruser.remove(self.username)
        

print(user.userc)

print(user.cruser)
pyn = user('poyan','mamadi')
ali = user('mamad','mamadian')
print(user.userc)
print(user.cruser)
ali.delete()
print(user.userc)
print(user.cruser)
ali = user('mamad','mamadian')
print(id(user.allowuser))
print(id(pyn.allowuser))
user.allowuser = ['poyan'] # pyn.allowuser = ['poyan'] its just change pyn
print(id(user.allowuser))
print(id(pyn.allowuser))
