class Apple():
    def get_name(self,name):
        self.name=name
    def what_self(self):
        print("my name is %s" %self.name)

a=Apple()
a.get_name('aaa')
a.what_self()
b=Apple()
b.get_name('bbb')
b.what_self()