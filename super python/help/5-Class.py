class persion():
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
    def display(self):
        print(self.name)
        print(self.idnum)


class emp(persion):
    def __init__(self, name, idnum, salary, post):
        persion.__init__(self, name, idnum)
        self.salary = salary
        self.post = post
    def emp(self):
        print("your are {} and your id num is {} and your salary is {} your jobp is {}".format(self.name, self.idnum, self.salary, self.post))


emp1 = persion("ali", 1)
emp2 = emp("reza", 1323, "20mil", "python programmer")
emp2.emp()