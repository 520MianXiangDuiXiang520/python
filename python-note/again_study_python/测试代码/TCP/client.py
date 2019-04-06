# 客户端
import socket
import sys

# 服务器地址与端口号
HOST='127.0.0.1'
PORT=57890
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    # 尝试连接远程服务器
    s.connect((HOST,PORT))
except Exception as e:
    print("服务端未开启")
    sys.exit()
while True:
    c=input("what you want to say:")
    # 向服务端发送请求消息
    s.sendall(c.encode())
    # 接受服务端反馈消息
    data=s.recv(1024)
    data=data.decode()
    print(data)
    if c.lower()=='bye':
        break
s.close()

