class user:
    
    username='user'
    password='0000000'
    def show_userpass(self):
        return f"{self.username} {self.password}"



numl = list()
print(type(numl))
poyan =user()
print(type(poyan))
print(poyan.show_userpass())