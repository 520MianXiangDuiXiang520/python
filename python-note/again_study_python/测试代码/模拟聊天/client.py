import socket
import threading
import os

def Send(s):
    while True:
        data = input('==>').encode()
        s.sendto(data, ('192.168.47.132', 5000))
        if data.decode().lower() == 'bye':
            os._exit(0)

def Recv(s):
    user={'192.168.47.132':'ubuntu'}
    while True:
        data, addr = s.recvfrom(1024)
        if addr[0] in user:
            print('\n 来自{0}的消息：{1}'.format(user[addr[0]],data.decode()))
        else:
            print('来自IP为{0}陌生人的消息：{1}'.format((addr[0]),data.decode()))
        if data.decode().lower() == 'bye':
            print("接收到中断消息，已停止运行程序")
            s.close()
            os._exit(0)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',5000))
thread_send=threading.Thread(target=Send,args=(s,))
thread_recv=threading.Thread(target=Recv,args=(s,))
thread_recv.start()
thread_send.start()


