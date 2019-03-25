class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("drink")
    def sleep(self):
        print("sleep")

class Dog(Animal):
    def wang(self):
        print("汪汪")

class SuperDog(Dog):
    def fly(self):
        print("飘呀飘呀，我的骄傲放纵")

wangcai=Dog()
xiaotianquan=SuperDog()
wangcai.eat()
wangcai.wang()
xiaotianquan.eat()
xiaotianquan.wang()
xiaotianquan.fly()