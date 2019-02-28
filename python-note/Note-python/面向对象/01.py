class study:
    name='zjb'
    id='001'
    def do(self):
        print("do")

    def do2(self):
        print("do2")

class study2:
    name='st2'
    id='002'
    def do(self):
        print("sty2_do")
    def do2(self):
        print("stu2_do2")

class study3(study2):
    s='oo'
    def hh(self):
        print("继承")

stu1=study()
stu2=study2()
stu3=study3()

print(stu1.id)
print(stu2.id)

stu1.do()
stu2.do()
stu3.do()