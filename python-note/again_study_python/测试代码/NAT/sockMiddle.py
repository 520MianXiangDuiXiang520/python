import socket
import threading

def middle(conn,addr):
    # 发起与服务器的连接
    sockDst=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockDst.connect(('192.168.47.130',1234))
    while True:
        data=conn.recv(1024).decode()
        print('收到客户端数据:'+data)
        sockDst.send(data.encode())
        print('转发给服务器')
        data_fromServer=sockDst.recv(1024).decode()
        print('接收到服务器的反馈:'+data_fromServer)
        conn.send(b'Server reply:'+data_fromServer.encode())
        print('转发给客户端')
    conn.close()
    sockDst.close()

def accept_client(sockScr):
    while True:
        try:
            # 响应客户端连接请求
            conn,addr=sockScr.accept()
            middle(conn,addr)
            print('新客户:'+str(addr))
        except:
            pass

def main():
    sockScr=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockScr.bind(('',12345))
    sockScr.listen(20)
    print('代理已启动')

    t1=threading.Thread(target=accept_client,args=(sockScr,))
    t2 = threading.Thread(target=accept_client, args=(sockScr,))
    t3 = threading.Thread(target=accept_client, args=(sockScr,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

if __name__ == '__main__':
    try:
        main()
    except:
        pass