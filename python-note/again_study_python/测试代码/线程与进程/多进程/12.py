# 管道

from multiprocessing import Process,Pipe

def demo1(pipe):
    left,right=pipe
    right.close()
    while True:
        try:
            s=left.recv()
            print(s)
        except:
            left.close()
            print('pipe close')
            break

def demo2(pipe):
    left,right=pipe
    left.close()
    for i in range(10):
        try:
            right.send(i)
        except:
            print('pipe close')
            break
    right.close()


if __name__ == '__main__':
    pipe=Pipe()
    left, right = pipe
    p1=Process(target=demo1,args=(pipe,))
    p2=Process(target=demo2,args=(pipe,))
    p1.start()
    p2.start()
    left.close()
    right.close()

