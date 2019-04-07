import threading
import time

def demo(x,y):
    print('%s 进程开始' % threading.current_thread().name)
    while x<=y:
        print(x,end='')
        x+=1
    time.sleep(2)
    print('函数执行完毕')

print('%s 进程开始'%threading.current_thread().name)
t1=threading.Thread(target=demo,args=(10,20),name='Thread 1')
t1.start()
# 等待被调用线程也就是t1结束后或者超时后再调用后续代码
t1.join(5)
t2=threading.Thread(target=demo,args=(1,10),name='Thread 2')
t2.start()


