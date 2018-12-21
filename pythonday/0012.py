# 用 Python 写一个爬图片的程序,将爬取到的图片放到 0012 文件夹下面
# https://cdn.pixabay.com/photo/2016/11/14/05/29/girl-1822702__340.jpg 1x, https://cdn.pixabay.com/photo/2016/11/14/05/29/girl-1822702__480.jpg 2x

import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring,tostring
import re
import os

# 从网页中爬取图片链接，保存到列表中
def getUrl(url,info):
    p_url=[]
    html=requests.get(url).text   # 得到最初网页源代码
    soup=BeautifulSoup(html,'html.parser')  # 格式化为标准HTML文本
    html_p = soup.find_all('div',attrs={'class':'item'})   # 过滤掉其他内容，只留下与图片相关的div标签信息
    html_p = repr(html_p)   # 把过滤之后的内容补充为HTML格式
    tree = fromstring(html_p)
    fixed_htmlp = tostring(tree, pretty_print=True)   # 得到补充好的
    soup=BeautifulSoup(fixed_htmlp,'html.parser')
    href=soup.find_all('img')
    href=repr(href)
    imc=re.findall(r'[a-zA-z]+://[^\s]*340.jpg',href)
    imc=set(imc)
    return imc

# 从列表中取出图片链接，爬取图片,存入文件夹

def getPicture(p_url,s):
    root = '0012//'
    path = root + repr(s) + ".jpg"
    try:
        # 判断更目录是否存在
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(p_url)
            with open(path, 'wb') as  f:
                f.write(r.content)
                print("第 "+repr(s)+" 个下载已完成")
        else:
            print("文件已存在")
    except:
        print("爬取失败")

if __name__ == '__main__':
    pathHead="https://pixabay.com/zh/photos/girl/?image_type=photo&pagi="
    page=1
    i=1
    info=[]
    for page in range(15):
        path=pathHead+repr(page+1)
        s=getUrl(path,info)
        print("第 "+ repr(page+1) +" 页URL获取完成，正在下载...")
        for p in s:
            getPicture(p, i*(page+1))
            i += 1
