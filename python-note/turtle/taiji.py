import turtle
turtle.setup(800,600)
turtle.pensize(10)
turtle.pencolor(0,0,0)
#turtle.goto(-100,100)
#turtle.goto(-100,-100)
#turtle.seth(45)#绝对角度
#turtle.left(45) 海龟角度左
#turtle.right(45)海龟角度右
#turtle.fd(150)
#turtle.penup()
#turtle.goto(-150,0)
#turtle.pendown()
#turtle.goto(150,0)
turtle.pu()
turtle.goto(0,-150)
turtle.pd()
turtle.circle(150)
turtle.circle(150/2,180)
turtle.circle(-150/2,180)
turtle.pu()
turtle.goto(0,150/2)
turtle.pd()
turtle.circle(1)
turtle.pu()
turtle.goto(0,-150/2)
turtle.pd()
turtle.circle(1)
turtle.done()