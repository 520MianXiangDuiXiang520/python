from PIL import Image,ImageFont,ImageDraw
import math

imc=Image.open('E:/桌面文件/安全/Lena.png')
cor=[]
h,w=imc.size
for x in range(h):
    for y in range(w):
        if imc.getpixel((x,y))!=(255,255,0):

            if imc.getpixel((x, y))[2] & 1:
            # if imc.getpixel((x,y))[2] & 0x01:
                print('---',imc.getpixel((x,y))[2] & 1)
                print('---', imc.getpixel((x, y))[2])
                cor.append(0)
            else:
                print('-----', imc.getpixel((x, y))[2]&1)
                print('-----', imc.getpixel((x, y))[2])
                cor.append(1)

width=int(math.sqrt(len(cor)))
print(width)
num=0
newimg = Image.new('RGB', (width, width))
for i in range(int(width)):
    for j in range(int(width)):
        if cor[num]==0:
            newimg.putpixel((i,j),(0,0,0))
        else:
            newimg.putpixel((i, j), (255, 255, 255))
        num+=1
newimg.save('new.jpg')
newimg.show()

