# 多线程中,所有变量由所有线程共享
import threading
import time

class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(0.5)
        global x,lock
        # 得到 锁,并把🔒的状态置为locked,其他线程阻塞在此,等待🔒被释放 ,只有拿到🔒才能执行后面的代码
        lock.acquire()
        try:
            x+=3
            print(x)
        finally:
            # 释放🔒
            lock.release()

lock=threading.RLock()

t1=[]
for t in range(5):
    s=Mythread()
    t1.append(s)
x=0
for t in t1:
    t.start()


