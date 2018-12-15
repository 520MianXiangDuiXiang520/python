#爬取豆瓣top 250


import requests
import bs4
from bs4 import BeautifulSoup
from lxml.html import fromstring,tostring
import re
import os

# 拼接10页URL

def get_url(page):
    url_begin="https://movie.douban.com/top250?"
    url_end="&filter="
    url_body="start="+repr(page)
    url=url_begin+url_body+url_end
    return url

# 得到HTML内容

def get_html(url):
    r=requests.get(url)
    html=r.text
    return html

# 得到排行榜相关的OL标签

def get_ol(html):
    soup=BeautifulSoup(html,'html.parser')
    ol=soup.find_all('ol',attrs={'class':'grid_view'})
    return ol

# 将ol标签补充称HTML格式，方便使用bs4

def get_ol_html(ol):
    ol=repr(ol)
    tree=fromstring(ol)
    fixed_ol=tostring(tree,pretty_print=True)
    return fixed_ol

# 得到与每个电影相关的li标签

def get_li(ol):
    soup=BeautifulSoup(ol,'html.parser')
    li=soup.find_all('li')
    li=list(li)
    return li

# 整理得到li标签中的信息

def get_info(li):
    soup=BeautifulSoup(li,'html.parser')
    name=soup.find_all('span',attrs={'class':'title'})
    name=repr(name)
    director=soup.find_all('p',attrs={'class':''})
    director=repr(director)
    score=soup.find_all('span',attrs={'class':'rating_num'})
    score=repr(score)
    jianping=soup.find_all('span',attrs={'class':'inq'})
    jianping=repr((jianping))
    info = {
        '片名': name+'\t',
        '': director,
        '评分': score,
        # '主演': actor,
        # '类型': kind,
        # '简介': final_summary,
         '简评': jianping
    }
    return info

#得到海报URL

def get_img_url(li):
    soup = BeautifulSoup(li, 'html.parser')
    scr=soup.find_all('img')
    scr=str(scr)
    r=r'(https://).+(.jpg)'
    url=re.finditer(r,scr)
    for urls in url:
        return urls.group()

# 爬取海报

def download_img(url_imc,i,j):
    root = '0005_豆瓣海报//'
    s=(i+1)*j
    path = root + repr(s)+".jpg"
    try:
        # 判断更目录是否存在
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url_imc)
            with open(path, 'wb') as  f:
                f.write(r.content)
                f.close()
        else:
            print("文件已存在")
    except:
        print("爬取失败")

# 前面函数有些乱，综合函数

def out():
    douban=""
    for i in range(10):
        url=get_url(i*25)
        html=get_html(url)
        ol=get_ol(html)
        fixed_ol=get_ol_html(ol)
        li=get_li(fixed_ol)
        for j in range(25):
            li = list(li)
            fixed_li = get_ol_html(li[j])
            info = get_info(fixed_li)
            img_url = get_img_url(fixed_li)
            download_img(img_url, i, j)
            douban = douban + repr(info) + '\n\n'
    return douban

# 用正则删除不需要的标签信息

def dele(tex):
    r1=r'<.+?>'
    r2=r'[\{\}\[\]\']'
    r3=r'[ \\xa0]'
    r4=r''
    text=re.sub(r1,"",tex)
    text=re.sub(r2,"",text)
    text = re.sub(r3, "", text)
    text = re.sub(r4, "", text)

    return text


if __name__ == '__main__':
    txt=out()
    clear=dele(txt)
    file = open('0005', 'a',encoding='utf-8')
    file.write(clear + '\n')
    print(clear)