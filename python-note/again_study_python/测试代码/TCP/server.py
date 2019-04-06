# 服务端

import socket

words={'how are you':'gun'}

# 服务端IP地址，为空时表示可以使用本机任何可用IP
HOST=''
# 服务器端口号，占用该端口与客户端通信
PORT=57890
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定地址和端口号
s.bind((HOST,PORT))
# 开始监听
s.listen(1)
print("正在监听端口 %d" % PORT)
# 监听发现有客户端请求建立连接，响应客户端请求，返回一个元组，包含一个socket对象和一个客户端信息，也是一个元组(hostaddr, port)
conn,addr=s.accept()
print(" 与 %s 建立了连接"% repr(addr[0]))
while True:
    # 接受客户端请求消息
    data=conn.recv(1024)
    data=data.decode()
    if not data:
        break
    print('Received message:',data)
    # 向客户端发送对应相应消息
    conn.sendall(words.get(data,'Nothing').encode())
# 关闭与客户端的连接
conn.close()
# 关闭服务器连接
s.close()