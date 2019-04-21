# 使用类创建进程
from multiprocessing import Process
import time
import os

def demo():
    print('孙子进程启动：pid：%d  父进程： %d'%(os.getpid(),os.getppid()))
    time.sleep(20)
    print('孙子进程结束：pid：%d  父进程： %d'%(os.getpid(),os.getppid()))

class MyProcess(Process):
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
    def run(self):
        print('子进程启动 pid  %d ,父进程：%d' % (os.getpid(),os.getppid()))
        a=Process(target=demo)
        # 设置守护进程
        a.daemon=True
        a.start()
        time.sleep(5)
        print('子进程结束 pid:%d ,父进程：%d' % (os.getpid(),os.getppid()))
if __name__ == '__main__':
    print('主进程启动，pid： %d'%os.getpid())
    q=MyProcess(1,2)

    q.start()
    print('主进程结束 pid: %d ' % os.getpid())


# 主进程启动，pid： 14584
# 主进程结束 pid: 14584
# 子进程启动 pid  18616 ,父进程：14584
# 孙子进程启动：pid：20728  父进程： 18616
# 子进程结束 pid:18616 ,父进程：14584