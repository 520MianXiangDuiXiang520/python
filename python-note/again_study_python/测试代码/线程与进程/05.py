# condition类

import threading
import time
import random

# 定义生产者线程类

class Producer(threading.Thread):
    """生产者线程类,负责在全局列表的尾部添加元素,如果列表长20,就调用wait让该线程等待"""
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        global x,con
        while True:
            con.acquire()
            if len(x)==20:
                # wait 将当前进程放入condition等待池,等待被唤醒,wait必须要得到锁才能使用
                con.wait()
                print("队列已满,生产者等待...")
            else:
                s=random.randint(10,10000)
                x.append(s)
                print('当前列表(生产者):', end='')
                print(x)
                time.sleep(1)
                # 用来唤醒进程,wait只能用notify唤醒
                con.notify()
            # 释放锁
            con.release()

class Consumer(threading.Thread):
    """消费者线程类,如果列表为空,消费者等待,否则弹出栈顶元素"""
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        global x,con
        while True:
            con.acquire()
            if not x:
                con.wait()
                print("消费者等待...")
            else:
                x.pop(0)
                print('当前列表(消费者):', end='')
                print(x)
                time.sleep(2)
                con.notify()
            con.release()

if __name__ == '__main__':
    con=threading.Condition()
    x=[]
    pro=Producer('生产者')
    cons=Consumer('消费者')
    cons.start()
    pro.start()

    pro.join()
    cons.join()
