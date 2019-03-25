class people:

    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
        print("他初始的体重是 %s kg" % self.weight)

    def run(self):
        self.weight=self.weight-1.5
        print("运动后的体重是 %s kg" % self.weight)

    def eat(self):
        self.weight=self.weight+2
        print("他吃后的体重是 %s kg" % self.weight)

    def __str__(self):
        return "这是 %s 的情况" % self.name

xiaoming=people('小米',75.5)
xiaohong=people('小红',45.5)
print(xiaoming)
print(xiaohong)
xiaoming.eat()
xiaohong.eat()
xiaoming.run()
xiaohong.run()


