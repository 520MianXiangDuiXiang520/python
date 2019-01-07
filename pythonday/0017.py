# 再 0016 的基础上增加显示时间的功能，使它更像一块表

import time
import pygame
import turtle

def 画线(线):
    turtle.penup()
    turtle.fd(8)
    if 线:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)   # 前进40
    turtle.penup()
    turtle.fd(8)
    turtle.right(90)   # 向右旋转90


def 画数字(数字):
    if 数字 in [2, 3, 4, 5, 6, 8, 9]:
        画线(True)
    else:
        画线(False)
    画线(True) if 数字 in [0, 1, 3, 4, 5, 6, 7, 8, 9] else 画线(False)
    画线(True) if 数字 in [0, 2, 3, 5, 6, 8, 9] else 画线(False)
    画线(True) if 数字 in [0, 2, 6, 8] else 画线(False)
    turtle.left(90)
    画线(True) if 数字 in [0, 4, 5, 6, 8, 9] else 画线(False)
    画线(True) if 数字 in [0, 2, 3, 5, 6, 7, 8, 9] else 画线(False)
    画线(True) if 数字 in [0, 1, 2, 3, 4, 7, 8, 9] else 画线(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def 画日期(日期):
    for i in 日期:
        if i=='N':
            turtle.write('年',font=("宋体",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=='Y':
            turtle.write('月', font=("宋体", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i=='R':
            turtle.write('日', font=("宋体", 18, "normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        elif i==':':
            turtle.write(':', font=("宋体", 18, "normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        else:
            画数字(eval(i))

def 播放歌曲(路径, 歌长):
    pygame.mixer.init()   # 初始化音频部分
    pygame.mixer.music.load(路径)   # 载入音乐
    pygame.mixer.music.play()   # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
    time.sleep(歌长)   # 延时一定的时间，等待播放完再停止
    pygame.mixer.music.stop()   # 停止播放

def 画表():
        turtle.setup(800, 700, 200, 200)
        turtle.setup(800, 700, 200, 200)
        turtle.speed(30)
        turtle.penup()
        turtle.goto(-350, 100)
        turtle.pensize(5)
        画日期(time.strftime('%YN%mY%dR', time.localtime()))
        turtle.goto(-300, -100)
        画日期(time.strftime('%H:%M:%S', time.localtime()))
        turtle.hideturtle()
        # turtle.done()
        # time.sleep(5)



if __name__ == '__main__':
    文件1 = r'E:\PYthon\pythonday\pythonday\0016\山间清晨.wav'
    文件2 = r'E:\PYthon\pythonday\pythonday\0016\百灵鸟音效.wav'
    画表()
    while(1):
        if (time.strftime('%S', time.localtime()) in ['07','17','27','37','47','57']):
            turtle.reset()
            画表()
        分钟=time.strftime('%M', time.localtime())
        if (分钟 == '30'):
            歌长=28
            播放歌曲(文件1, 歌长)
            time.sleep(60 - 歌长)
        if(分钟=='00'):
            歌长 = 5
            播放歌曲(文件2, 歌长)
            time.sleep(60 - 歌长)
