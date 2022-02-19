class base():
    def __init__(self):
        self.str1 = "amir"
        print("base1")

class base2():
    def __init__(self):
        self.str2 = "mohamad"
        print("base2")

class tarkib(base, base2):
    def __init__(self):
        base.__init__(self)
        base2.__init__(self)
        print("Tarkib")
    def pstr(self):
        print(self.str1, self.str2)

obj = tarkib()
obj.pstr()