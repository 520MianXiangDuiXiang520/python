import socket
import sys
import struct
import getpass

def main(serverIP):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((serverIP,10600))
    userId=input('输入用户名：')
    userPwd=getpass.getpass('请输入密码：')
    message=userId+',' + userPwd
    sock.send(message.encode())
    login=sock.recv(100)
    if login==b'error':
        print('用户名或密码错误！')
        return
    intSize=struct.calcsize('I')
    while True:
        command=input('##>').lower().strip()
        if not command:
            continue
        command=''.join(command.split())
        sock.send(command.encode())
        if command in('q','quit'):
            break
        elif command in('list','dir','ls'):
            loc_size=struct.unpack('I',sock.recv(intSize))[0]
            files=eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        elif command in('cd','cwd'):
            print(sock.recv(1024).decode())
        elif command.startswith('cd'):
            print('打开目录')
            print(sock.recv(100).decode())
        elif ''.join(command.split())=='cd..':
            print('返回上一级')
            print(sock.recv(100).decode())
        elif command.startswith('get'):
            isFileExist=sock.recv(20)
            if isFileExist != b'ok':
                print('error')
            else:
                print('downloading.',end='')
                # print(command.split())
                fp=open(command.split('get')[1],'wb')
                while True:
                    print('.',end='')
                    data=sock.recv(4096)
                    if data ==b'overxxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
        else:
            print("无效")
    sock.close()

if __name__ == '__main__':
    serverIp=sys.argv[1]
    main(serverIp)
