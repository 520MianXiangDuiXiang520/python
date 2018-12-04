#蒙特卡洛方法求圆周率
from random import random
from time import perf_counter
#随机生成两个0-1的数，作为坐标
start=perf_counter()
cricle=0.000
for i in range(10000*1000):
    x,y=random(),random()
    r=pow(x ** 2+y ** 2,0.5)
    if r<=1:
        cricle=cricle+1
pi=cricle/10000000
print(pi*4)
t=perf_counter()-start
print("蒙特卡洛运行时长：",t)
start=perf_counter()
pi2=0
N=1000
for i in range(N):
    pi2=pi2+(1/pow(16,i))*((4/(8*i+1))-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print(pi2)
t=perf_counter()-start
print("公式运行时长:{}".format(t))