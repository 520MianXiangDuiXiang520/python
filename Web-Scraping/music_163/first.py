# 首先打算爬取到歌手以及作评的id

import requests
import bs4
from bs4 import BeautifulSoup
from lxml.html import fromstring,tostring
import re
import os
import time

url='https://music.163.com/#/discover/artist/signed/'   # 网易云音乐入驻歌手

# class=m-cvrlst m-cvrlst-5 f-cb,id=m-artist-box

def get_ul():
    url = 'https://music.163.com/#/discover/artist/signed/'  # 网易云音乐入驻歌手
    req=requests.get(url)
    time.sleep(10)
    html=req.text
    print(html)
    Soup=BeautifulSoup(html,'html.parser')
    ul = Soup.find_all('ul')
    print(ul)
    return ul

if __name__ == '__main__':
    get_ul()