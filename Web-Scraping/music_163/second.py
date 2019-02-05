# 首先打算爬取到歌手以及作评的id

import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring,tostring
from urllib.request import urlretrieve


def song(url):
    id_list = []
    name_list=[]
    headers = {'Host': 'music.163.com',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content - Type': 'application / x - www - form - urlencoded',
               'Content - Length': '340',
               'Cache - Control': 'max - age = 0',
               'Cookie': 'JSESSIONID-WYYY=dCYq9jVg67nSVCCTjqH5tYIQv2IdFZze425qd6DYKM7ZGny0wiM%2Ber3cIksIp6RU6Et9PfoqY4ynxubWRUAJ6v%2B8odx%2F7GYEGG%5Cbpq0v%2FqrY7yokmngDiInZBPDz1d7bZxjkZW8aiMC5jj%5Cgig7TJ4p%2BTzTqlugDJMxChHxeK%2ByZqy%5CK%3A1549352253864; _iuqxldmzr_=32; _ntes_nnid=7fff421235022c5dfe3cba199f702822,1549350453885; _ntes_nuid=7fff421235022c5dfe3cba199f702822; WM_NI=7n2V78OQ%2BkhVDHhadVHANe8nXD7BT1Q1ZNahjJVh7hZVXhd3%2F4Mo4qP%2Bgo1Az9ZQrkkY4%2FkAz1wYPyuytAySNmgVn3okb%2FHE%2Fb%2BZOC1Cj%2Bx3cFFX5MpsLFw0Pp2OXtNhVm8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed6e53eedb297bbe63ef1968ba3c44e879f9baaf37d8bf5ff86f77ef1ba8490c82af0fea7c3b92af5b2feb7b6348d8fe58ceb5e8898a882e75e8c9f8286bb669c9cf9a3d73b93ef96afe464aa969a89b6649a8a9889e739edec8390b77b94f5a990b44bbae796b2f161a987fcd0ea4bbaefb9bad373b7a7bca2fc598eb3a9b7ed39adb5aed0cb4fedbee5bbce49f39da6ccfb39a19a8ab9b847b4ad84a7f63c94b0feb0db808eb89a8ebb37e2a3; WM_TID=e4GH8XbWYNpBRQAEEQJshJuwL8vzeetE',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    r=requests.get(url,headers=headers)
    text=r.text
    #print(text)
    soup = BeautifulSoup(text, 'html.parser')
    s=soup.find_all('ul', attrs={'class': 'f-hide'})

    s=repr(s[0])
    tree=fromstring(s)
    s=tostring(tree,pretty_print=True)
    soup=BeautifulSoup(s,'html.parser')
    s=soup.find_all('a')
    #print(s[0])
    r='[0-9]+.+[\u4e00-\u9fa5]'
    d='">'
    n='[0-9]+'
    nam='[\u4e00-\u9fa5]+'
    for i in s:
        try:
            s=re.findall(r,repr(i))
            #print(repr(s[0]))
            s=re.sub(d,"",repr(s[0]))
            #print(s)
            id=re.findall(n,s)
            name=re.findall(nam,s)
            id_list.append(id[0])
            name_list.append(name[0])
        except:
            continue
    dit = dict.fromkeys(id_list, "1")
    for a in range(len(id_list)):
        dit[id_list[a]]=name_list[a]
    return dit

# http://music.163.com/song/media/outer/url?id=317151.mp3

def download(dit):
    for id in dit.keys():
        downloadurl='http://music.163.com/song/media/outer/url?id='+id
        path='E:\PYthon\pythonday\Web-Scraping\music_163\music\%s.mp3'%dit[id]
        try:
            print("正在下载%s"%dit[id])
            urlretrieve(downloadurl,path)
            print("下载完成。。。")
        except:
            continue


if __name__ == '__main__':
    inputip=input("请输入要下载的歌手id,通过first.py查询，改天完善")

    url='https://music.163.com/artist?id='+inputip
    print(url)
    dit=song(url)
    download(dit)
        #print(i)


# https://music.163.com/artist?id=8103

