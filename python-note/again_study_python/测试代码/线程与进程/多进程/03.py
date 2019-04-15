# 使用函数创建进程
from multiprocessing import Process
import time
import os

def demo(x,y):
    StartTime=time.time()
    print('%s start ...'%os.getpid())
    print(x+y)
    time.sleep(2)
    print('%s end runs %0.2f s'%(os.getpid(),(time.time()-StartTime)))

if __name__ == '__main__':
    s=Process(target=demo,args=(1,2))
    d=Process(target=demo,args=(3,4))
    s.start()
    d.start()
    print('main')