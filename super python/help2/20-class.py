class person:
    test = 123
    def __init__(self,name,fml,age):
        self.name = name
        self.family = fml
        self.age = age
    def show_fln(self):
        return f'{self.name} {self.family}'
class teacher(person):
    pass


pyn=person('poyan','mamadi',39)

print(pyn.name)

ali = teacher('ali','mamadian',35)
print(ali.name)
print(teacher.test)

print(ali.show_fln())