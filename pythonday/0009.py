# 制作一个简单的随机验证码
# truetype()  加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。
# draw.text() 文字的绘制，第一个参数指定绘制的起始点（文本的左上角所在位置），第二个参数指定文本内容，第三个参数指定文本的颜色，第四个参数指定字体（通过ImageFont类来定义）。
# draw.line() 直线的绘制，第一个参数指定的是直线的端点坐标，形式为（x0, y0, x1, y1），第二个参数指定直线的颜色；
# draw.arc() （椭）圆弧的绘制，第一个参数指定弧所在椭圆的外切矩形，第二、三两个参数分别是弧的起始和终止角度， 第四个参数是填充颜色，第五个参数是线条颜色；
from PIL import Image,ImageFont,ImageDraw
import random
import string

# 产生随机字母

def getRandword(length):
     dic=string.ascii_uppercase+string.ascii_lowercase
     key=""
     for i in range(length):
        key=key+random.choice(dic)+" "
     return key

# 产生随机颜色

def getRandcolor():
    r=random.randrange(0,255)
    g=random.randrange(0,255)
    b=random.randrange(0,255)
    return r,g,b

def getRandnum():
    x1 = random.randrange(1, 100)
    y1 = random.randrange(2, 59)
    x2 = random.randrange(100, 198)
    y2 = random.randrange(2, 58)
    return x1,y1,x2,y2

if __name__ == '__main__':
    ima=Image.new('RGB',(200,60),(255,255,255))
    ft=ImageFont.truetype('font/BAUHS93.TTF',55)
    draw=ImageDraw.Draw(ima)
    for j in range(4):
        text=getRandword(1)
        draw.text((10+50*(j),-5),text,getRandcolor(),ft)
    for line in range(2):
        draw.line(getRandnum(),getRandcolor())
    for arc in range(4):
        a1=random.randrange(0,90)
        a2=random.randrange(0,90)
        draw.arc(getRandnum(),a1,a2,getRandcolor())
    for plot in range(6000):
        a1 = random.randrange(0, 200)
        a2 = random.randrange(0, 60)
        draw.point((a1,a2),getRandcolor())
    ima.show()
    ima.save('0009.jpeg','jpeg')