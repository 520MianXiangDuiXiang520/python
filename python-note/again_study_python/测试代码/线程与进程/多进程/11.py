# 队列

from multiprocessing import Process,Queue
import time
import random

def Producer(q):
    '''生产者类，超过20等待'''
    while True:
        if not q.full():
            food=random.randint(1,100)
            print('生产%d'%food)
            q.put(food)
            time.sleep(1)
        else:
            print('q is full')


def Consumer(q):
    while True:
        if not q.empty():
            s=q.get()
            print('消费:%d'%s)
            time.sleep(2)
        else:
            print('q is empty')

if __name__ == '__main__':
    q=Queue(20)
    q1=Process(target=Producer,args=(q,))
    q2=Process(target=Consumer,args=(q,))
    q1.start()
    q2.start()