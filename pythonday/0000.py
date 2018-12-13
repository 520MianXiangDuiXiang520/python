#   2018/12/12
#第0000题：将图片左上角加上红色数字
#使用PIL完成图片处理
from PIL import Image, ImageDraw, ImageFont

im=Image.open('0000/0000.jpg','r')
#打开图片

#im.show()

#保存图片

#im.save("0000/0000.jpeg",'jpeg')

#裁剪图片,xy为裁剪的坐标

#xy=(10,10,100,100)
#imcut=im.crop(xy)
#imcut.show()
#imcut.save("0000/cut.jpeg",'jpeg')

#图片拼合
#把imc拼接到 backgroundimc 的（200，200）处

#backgroundimc=im
#imc=Image.open('0000/cut.jpeg')
#backgroundimc.paste(imc,(200,200))
#backgroundimc.show()
#backgroundimc.save('0000/paste.jpeg','jpeg')

#图片缩放

#(x,y)=im.size
#change_x=1200
#注意，//！！change_x,change_y参数需要时整数，不能用“/”。要用“//”
#change_y=y*change_x//x
#out=im.resize((change_x,change_y),Image.ANTIALIAS)
#out.show()
#out.save('0000/resize.jpeg','jpeg')

#在图片上写字
#imagefont参考csdn，https://blog.csdn.net/icamera0/article/details/50762050
text='1'
imtext=Image.open('0000/cut.jpeg')
imtext_chinese=im
draw = ImageDraw.Draw(imtext)
font = ImageFont.truetype('./simhei.ttf',45)
draw.text((60,10),text, font=font,fill=(255,0,0))
imtext.show()
imtext.save("0000/text.jpeg",'jpeg')
draw = ImageDraw.Draw(imtext_chinese)
font = ImageFont.truetype('./simhei.ttf',75)
draw.text((60,10),u'面向对象', font=font,fill=(255,0,0))
imtext_chinese.show()
imtext_chinese.save("0000/text_chinese.jpeg",'jpeg')