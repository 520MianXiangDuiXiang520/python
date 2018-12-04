import turtle
import time
import os
#绘制一段数码管
def drawline(draw):
    turtle.penup()
    turtle.fd(8)
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)#前进40
    turtle.penup()
    turtle.fd(8)
    turtle.right(90)#向右旋转90


def drawDigit(digit):
    if digit in [2,3,4,5,6,8,9]:
        drawline(True)
    else:
        drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    for i in date:
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
            drawDigit(eval(i))

def main():
    while 1==1:
        turtle.setup(800, 700, 200, 200)
        turtle.penup()
        turtle.goto(-350,100)
        turtle.pensize(5)
        drawDate(time.strftime('%YN%mY%dR',time.localtime()))
        turtle.goto(-300, -100)
        drawDate(time.strftime('%H:%M:%S', time.localtime()))
        turtle.hideturtle()
        #turtle.done()
        time.sleep(5)
        turtle.reset()
main()





