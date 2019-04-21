# Pool
from multiprocessing import Process,Pool
import time

def demo(x):
    print('start ..%d'%x)
    time.sleep(2)
    print('%d end'%x)


if __name__ == '__main__':
    print('main start')
    starttime=time.time()
    P=Pool(4)
    for i in range(4):
        P.apply(demo,args=(i,))

    P.close()
    P._state= 0
    P.apply_async(demo,args=(5,))
    P._state=1
    P.join()
    print('main end uned time is %.2lf'%(time.time()-starttime))


# main start
# start ..0
# 0 end
# start ..1
# 1 end
# start ..2
# 2 end
# start ..3
# 3 end
# main end uned time is 8.78