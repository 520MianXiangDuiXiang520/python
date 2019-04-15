import threading
import time

def demo():
    print('%s 线程开始'% threading.current_thread().name)
    n=0
    while n<4:
        n+=1
        print('%s 线程运行 》》》 %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('%s 线程结束'% threading.current_thread().name)

print('%s 线程开始'%threading.current_thread().name)
t=threading.Thread(target=demo,name='N01')
t.start()
t.join()
print('%s 线程结束' % threading.current_thread().name)