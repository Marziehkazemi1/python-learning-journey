class Computer:
    count = 0

    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu


class Laptop(Computer):
    def value(self):
        return self.ram + self.hard + self.cpu + self.size


pc1 = Computer(12, 2, 4)
print(pc1.value())