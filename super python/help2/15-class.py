class user:
    def __init__(self,username,userpass='.us'):
        self.username = username
        self.userpass = userpass
    def show_card(self):
        return self.username + self.userpass

masih=user('M1778')

print(masih.username)
print(masih.show_card())