import threading
import time

def demo():
    time.sleep(2)
    print("this is thread---- %s" %threading.current_thread().name)

if __name__ == '__main__':
    start_time=time.time()
    threads=[]
    for t in range(5):
        t1=threading.Thread(target=demo)
        threads.append(t1)
    # 守护进程，当子进程设置为守护进程时，主进程结束，不管子进程有没有执行完毕，直接杀死子进程
    # 如果子进程不是守护模式，主进程结束后直接退出，子进程结束后才退出
    # 用setDaemon和daemon都可以设置守护进程
    # t1.setDaemon(True)
    for t1 in threads:
        t1.daemon=True

    for t1 in threads:
        t1.start()
    # 使用join使主线程在任务结束之后处在阻塞状态,等待子线程任务结束之后再退出
    for t1 in threads:
        # timeout是给每一个线程一个timeout,主线程总的timeout就是所有子线程timeout之和
        # 如果在timeout时间内子线程没有运行结束就会被杀死
        t1.join(0.4)
    print('主进程结束，用时：%lf ' %(time.time()-start_time))