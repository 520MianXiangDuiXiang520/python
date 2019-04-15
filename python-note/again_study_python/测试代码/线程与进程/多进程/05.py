from multiprocessing import Process
n=100
def demo():
    global n
    n=0
    print('demo:%d'%n)

if __name__ == '__main__':
    print('main %d' % n)
    p=Process(target=demo)
    p.start()