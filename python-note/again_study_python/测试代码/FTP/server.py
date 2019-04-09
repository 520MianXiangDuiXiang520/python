import socket
import threading
import os
import struct

users={
    'zhangsan':{'pwd':'zs12345','home':r'E:\PYthon\pythonday\python-note\again_study_python'},
    'lisi':{'pwd':'ls12345','home':r'E:\PYthon\pythonday\python-note\again_study_python'}
}
def server(conn,addr,home):
    print('新客户端：'+str(addr))
    os.chdir(home)
    while True:
        data=conn.recv(100).decode().lower()
        print(data)
        if data in('quit','q'):
            break
        elif data in ('list','dir','ls'):
            files=str(os.listdir(os.getcwd()))
            files=files.encode()
            conn.send(struct.pack('I',len(files)))
            conn.send(files)
        elif ''.join(data.split())=='cd..':
            cwd=os.getcwd()
            newCwd=cwd[:cwd.rindex('\\')]
            if newCwd[-1]==':':
                newCwd+='\\'
            if newCwd.lower().startswith(home):
                os.chdir(newCwd)
                conn.send(b'ok')
            else:
                conn.send(b'error')
        elif data in ('cwd','cd'):
            conn.send(str(os.getcwd()).encode())
        elif data.startswith('cd'):
            data=data.split('cd')
            if len(data)==2 and os.path.isdir(data[1]):
                os.chdir(data[1])
            else:
                conn.send(b'error')
        elif data.startswith('get'):
            # data=data.split(maxsplit=1)
            data = data.split('get')
            print(data)
            if len(data)==2 and os.path.isfile(data[1]):
                conn.send(b'ok')
                fp=open(data[1],'rb')
                while True:
                    content=fp.read(4096)
                    if not content:
                        conn.send(b'overxxxxx')
                        break
                    conn.send(content)
                    if conn.recv(10)==b'ok':
                        continue
                fp.close()
            else:
                conn.send(b'no')
        else:
            pass

    conn.close()
    print(str(addr)+'关闭连接')


if __name__ == '__main__':
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('',10600))
    sock.listen(5)
    while True:
        conn,addr=sock.accept()
        print('与 %s 建立连接' %addr[0])
        userId,userPwd=conn.recv(1024).decode().split(',')
        if userId in users and users[userId]['pwd']==userPwd:
            conn.send(b'ok')
            home=users[userId]['home']
            t=threading.Thread(target=server,args=(conn,addr,home))
            t.daemon=True
            t.start()
        else:
            conn.send(b'error')