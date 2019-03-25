class A(object):
    @staticmethod
    def static_fun():
        print('这是一个静态方法')

a=A()
a.static_fun()
A.static_fun()