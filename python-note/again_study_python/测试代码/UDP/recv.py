# 接收端

import socket

# IPv4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定端口和端口号
s.bind(('',5000))

while True:
    data,addr=s.recvfrom(1024)
    print('接收到消息{0},发送端：{1}发送端口：{2}'.format(data.decode(),addr[0],addr[1]))
    if data.decode().lower()=='bye':
        print("接收到中断消息，已停止运行程序")
        break