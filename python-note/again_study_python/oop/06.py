class A:
    dan=None
    def __new__(cls, *args, **kwargs):
        if A.dan is None:
            print("分配空间")
            A.dan=super().__new__(cls)
        return A.dan

    def __init__(self):
        print("初始化对象")

a=A()
print(a)
b=A()
print(b)