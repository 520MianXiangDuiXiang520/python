# 守护进程
from multiprocessing import Process
import time
import os

def demo():
    print('%d start father is %d'%(os.getpid(),os.getppid()))
    time.sleep(2)
    print('%d end father is %d'%(os.getpid(),os.getppid()))

if __name__ == '__main__':
    print('main')
    p=Process(target=demo)
    p.daemon=True
    p.start()
    time.sleep(1)
    print('main end')

# main
# 11920 start father is 3516
# main end