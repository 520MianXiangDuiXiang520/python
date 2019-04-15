# 孤儿进程
from multiprocessing import Process
import time
import os

def demo():
    StartTime=time.time()
    print('%d process start,father is %d  time is %.2f'%(os.getpid(),os.getppid(),StartTime))
    time.sleep(1)
    print('%d process end father is %d time is %.2f'%(os.getpid(),os.getppid(),time.time()))

if __name__ == '__main__':
    p=Process(target=demo)
    print('father process is %d'%os.getpid())
    p.start()
    print('father process is %d' % os.getpid())