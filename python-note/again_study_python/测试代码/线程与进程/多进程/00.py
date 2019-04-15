from multiprocessing import Process
import time
import os

def demo():
    starttime=time.time()
    print(' %s start,time is %.2lf'%(os.getpid(),starttime))
    time.sleep(10)
    print('%s end,time is %.2lf,using time %.2lf'%(os.getpid(),time.time(),time.time()-starttime))

if __name__ == '__main__':
    s=Process(target=demo)
    s1=Process(target=demo)
    s.start()
    s1.start()
    print('%s正在运行'%s.name)
    print('%s正在运行' % s1.name)
    s.kill()
    s.join()
    print('end')
