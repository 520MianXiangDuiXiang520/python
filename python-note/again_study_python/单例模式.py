# class DanLi:
#     __add=None
#     def __new__(cls, *args, **kwargs):
#         if cls.__add is None:
#             cls.__add=super().__new__(cls)
#         return cls.__add
#
#     def __init__(self):
#         print('实例化对象')
#
# if __name__ == '__main__':
#     s1=DanLi()
#     s2=DanLi()
#     print(s1)
#     print(s2)

# 要在不修改原函数的情况下修饰demo

# def test(func):
#     def s(*args):
#         print('*'*100)
#         t=func(*args)
#         print('*'*100)
#         return t
#     return s
#
#
#
# @test
# def demo(name,list):
#     print('my name is %s'%name)
#     for i in range(10):
#         list.append(i)
#     print(list)
#     return list
#
# @test
# def sssa():
#     print("pppp")



# l=[i for i in range(9)]
# s=demo('zhan',l)

def DanLi(cla):
    _cladir={}

    def dan(*args,**kwargs):
        if cla not in _cladir:
            _cladir[cla]=cla(*args,**kwargs)
            print(_cladir[cla])
        return _cladir[cla]
    return dan

@DanLi
class Demo2:
    def __init__(self):
        print('class2')

@DanLi
class Demo1:
    def __init__(self):
        print('class1')

d=Demo2()
print("*"*100)
d2=Demo1()
print("*"*100)
d3=Demo2()
# print(d)
# print("*"*100)
# print(d2)
# print("*"*100)
# print(d3)


