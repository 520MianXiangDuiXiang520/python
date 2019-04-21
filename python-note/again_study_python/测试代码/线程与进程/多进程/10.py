# 进程锁

import time
from multiprocessing import Process,Lock

def demo(lock,name):
    lock.acquire()
    for i in range(10):
        time.sleep(1)
        print('%d---%s'%(i,name))
    lock.release()

def demo2(lock,name):
    lock.acquire()
    for i in range(10,20):
        time.sleep(1)
        print('%d***%s' % (i, name))
    lock.release()

if __name__ == '__main__':
    lock=Lock()
    p1=Process(target=demo,args=(lock,'p1',))
    p2 = Process(target=demo2, args=(lock,'p2',))
    p1.start()
    p2.start()
