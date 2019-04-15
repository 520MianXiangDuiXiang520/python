#图片爬去
import requests
import os
head={'user-agent':'Mozilla/5.0'}
url="https://h1.ioliu.cn/bing/YukonEmerald_ZH-CN1893750172_1920x1080.jpg"
#url="https://mooc1-2.chaoxing.com/mycourse/studentstudy?chapterId=126464177&courseId=202147626&clazzid=4981118&enc=5d15c8924e9595a072e1aa710541d5f7"
root='E://桌面文件//py//'
path=root+url.split('/')[-1]
try:
    #判断更目录是否存在
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        print(path)
        r=requests.get(url,headers=head)
        with open(path,'wb') as  f:
            f.write(r.content)
            f.close()
            print("success!")
    else:
        print("文件已存在")
except:
    print("爬取失败")