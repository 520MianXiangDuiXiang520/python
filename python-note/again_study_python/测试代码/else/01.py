class Demo:
    def __init__(self):
        self.x=0
        self.y=1
    def __next__(self):
        _mid=self.x
        self.x=self.y
        self.y=_mid+self.y
    def __iter__(self):
        return self

if __name__=="__main__":

    d=Demo()
    for i in d:
        if d.x<100000000:
            print(d.x,end="   ")