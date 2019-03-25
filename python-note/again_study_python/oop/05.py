class A:
    # 定义类属性
    sum=0
    # 定义类方法
    @classmethod
    def class_fun(cls):
        # 通过 cls 调用类属性
        print(cls.sum)
        print("这是一个类方法")
    @classmethod
    def class_fun2(cls):
        # 通过 cls 调用类方法
        cls.class_fun()
        print("这是另一个类方法")

    @staticmethod
    def static_fun():
        print("这是一个静态方法")

    def __init__(self,name):
        # 定义实例属性
        self.name=name
        # 调用类属性
        A.sum+=1


a=A('a')
b=A('b')
print("访问实例属性：   "+a.name)
print("通过类名访问类属性：   "+repr(A.sum))
print("通过实例对象名访问类属性   "+repr(a.sum))
print('通过类名访问类方法：   ')
A.class_fun()
print('通过实例对象名访问类方法')
a.class_fun2()
print('通过类名访问静态方法：   ')
A.static_fun()
print('通过实例对象名访问静态方法')
a.static_fun()