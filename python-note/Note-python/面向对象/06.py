class A:
    def f_a(self):
        print("我是A的方法")

class B:
    def f_b(self):
        print("我是B的方法")

class C(A,B):
    pass

class D(C):
    def f_d(self):
        print('好乱！！')

a=A()
b=B()
c=C()
d=D()

a.f_a()
b.f_b()
c.f_a()
c.f_b()
d.f_b()
d.f_a()
d.f_d()
