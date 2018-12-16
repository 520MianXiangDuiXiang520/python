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

def openimc(mic_name,weight,hight,name,file):
    picture=Image.open(mic_name)
    (x,y)=picture.size
    out=picture.resize((weight,hight),Image.ANTIALIAS)
    yes_or_no=os.path.exists('0006_图片缩放/'+file)
    if(yes_or_no==False):
        os.makedirs('0006_图片缩放/'+file, 0o777)
    out.save('0006_图片缩放/' + file+"/"+name, 'jpeg')

# 选择手机

def chose():
    print("\t\t\t 1.iphone 5")
    print("\t\t\t 2.iphone x")
    print("\t\t\t 3.huawei Mate 20")
    print("\t\t\t 4.OPPO Find X")
    type=input("请选择要缩放的手机型号：")
    if(type=='1'):
        width=1136
        hight=640
        path_son='iphone 5'
    elif(type=='2'):
        width=2436
        hight=1125
        path_son='iphone x'
    elif(type=='3'):
        width=2244
        hight=1080
        path_son='huawei Mate 20'
    elif(type=='4'):
        width=2340
        hight=1080
        path_son='OPPO Find X'
    else:
        print("不支持！")
        return 0
    return width,hight,path_son


if __name__ == '__main__':
    path='0005_豆瓣海报/'
    name=all_mic(path)                   # 获得以列表返回的图片名
    cho=chose()                        # 获得选择手机的相关信息
    for i in name:
        openimc(path+i,cho[0],cho[1],i,cho[2])




