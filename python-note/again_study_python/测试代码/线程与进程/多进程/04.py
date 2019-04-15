# 使用类创建进程
from multiprocessing import Process
import time
import os

class MyProcess(Process):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
    def run(self):
        StartTime=time.time()
        print('%s start'%self.name)
        print(self.x+self.y)
        time.sleep(2)
        print('%s end runs %0.2f s' % (self.name, (time.time() - StartTime)))

if __name__ == '__main__':
    q=MyProcess(1,2)
    d=MyProcess(3,4)
    q.start()
    d.start()
