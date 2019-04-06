# 获取鼠标所处窗口的文本

from ctypes import *
from ctypes import wintypes
from time import sleep

user32=windll.user32
p=wintypes.POINT()
buffer=create_string_buffer(255)

while True:
    sleep(0.5)
    user32.GetCursorPos(byref(p))
    HWnd=user32.WindowFromPoint(p)
    sleep(0.2)
    user32.SendMessageA(HWnd,13,255,byref(buffer))
    print(buffer.value.decode('gbk'))