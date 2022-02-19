class ensan():
    def __init__(self, name, vazn, ghad, age, test):
        self.name = name
        self.vazn = vazn
        self.ghad = ghad
        self.age = age
        ensan.test = test
    def get_name(self):
        print("your object name is %s" % self.name)

    def get_vazn(self):
        print("vaznet ine %s" % self.vazn)

    def ghad_age(self):
        print("GHAD SHOMA IS %s sen shoma is %s" % (self.ghad, self.age))

moalem = ensan("amir", 68, 173, 18, "this is test")
moalem.get_name()
moalem.get_vazn()
moalem.ghad_age()

karmand = ensan("reza", 80, 180, 30, "this is test")
karmand.ghad_age()
karmand.get_vazn()
karmand.get_name()