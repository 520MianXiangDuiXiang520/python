# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
from PIL import Image

# 遍历文件夹把所有照片以列表形式返回

def all_mic(path):
    mic=[]
    for micname in os.listdir(path):
        mic.append(micname)
    return mic

# 打开图片

def openimc(mic_name,weight,hight,name):
    picture=Image.open(mic_name)
    (x,y)=picture.size
    out=picture.resize((weight,hight),Image.ANTIALIAS)
    out.save('E:/桌面文件/媒体/图片/小/' "/"+name, 'jpeg')

# 选择手机




if __name__ == '__main__':
    path='E:/桌面文件/媒体/图片/23746张敏军 张玉珊/'
    name=all_mic(path)                   # 获得以列表返回的图片名
    for i in name:
        openimc(path+i,1500,2276,i)




