# 发送端
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(input('send').encode(),('192.168.47.1',5000))
s.close()