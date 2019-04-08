import socket
import threading


def replyMessage(conn):
    while True:
        # 接受代理发过来的消息原样返回
        data = conn.recv(1024)
        conn.send(data)
        print('接收到数据 %s' % data.decode())
        if data.decode().lower() == 'bye':
            print('断开连接')
            break
    conn.close()


def accept_middle(sockScr):
    while True:
        conn, addr = sockScr.accept()
        print('服务器已启动')
        print("与 %s 建立连接" % addr[0])
        replyMessage(conn)


def main():
    # TCP
    sockScr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockScr.bind(('', 1234))
    sockScr.listen(20)
    t1 = threading.Thread(target=accept_middle, args=(sockScr,))
    t2 = threading.Thread(target=accept_middle, args=(sockScr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()