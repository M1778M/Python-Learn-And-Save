class pc():
    def __init__(self, ram, hard, cpu, graphic):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu
        self.graphic = graphic

    def pc_value(self):
        print(self.ram + self.hard + self.graphic + self.cpu)

pc1 = pc(6, 256, 7, 1080)

pc1.pc_value()

class laptop(pc):
    def get_ram(self):
        print("ram is {}".format(self.ram))

laptop1 = laptop(16, 512, 9, 2060)
laptop1.pc_value()


class ult(laptop, pc):
    pass

utl1 = ult(2, 100, 4, 560)

utl1.pc_value()

utl1.get_ram()

