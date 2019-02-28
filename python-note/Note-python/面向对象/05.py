import random
class Fish:
    def __init__(self):
        self.x=random.randint(0,20)
        self.y=random.randint(0,20)

    def move(self):
        self.x-=1
        print(self.x,self.y)

class Goldfish(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(Fish)
        super().__init__()
        self.hunger= True

    def eat(self):
        if self.hunger:
            print("饿了，要吃！！")
            self.hunger=False
        else:
            print("没饿，不吃！！")


fish=Fish()
fish.move()
goldfish=Goldfish()
goldfish.move()
shark=Shark()
shark.eat()
shark.move()
shark.eat()