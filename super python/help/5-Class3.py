class base():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

class child(base):
    def __init__(self, name, age):
        base.__init__(self, name)
        self.age = age
    def get_age(self):
        return self.age
class grandchild(child):
    def __init__(self, name, age, addr):
        child.__init__(self, name, age)
        self.addr = addr

    def get_addr(self):
        return self.addr()
obj1 = grandchild("serena", 26, "tehran")

print(obj1.get_name(), obj1.get_age(), obj1.get_addr())