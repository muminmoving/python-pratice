import random
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for i in range(1, 11):
            num = random.randint(1, self.sides)
            print(num)

class Die_1(Die):
    def __init__(self, sides=10):
        super().__init__()
        self.sides = sides

die_1 = Die_1()
die_1.roll_die()
