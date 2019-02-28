class noodles():
    n='nn'
    o='oo'
    __d='dd'
    def get_d(self):
        print(self.__d)

Noodle=noodles()

print(Noodle.n)
print(Noodle.o)
#print(Noodle.__d)
print(Noodle._noodles__d)
Noodle.get_d()