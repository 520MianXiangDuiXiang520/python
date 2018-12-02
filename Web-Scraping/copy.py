# -*- coding: utf-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup

base_url = 'http://www.dianping.com'
url = 'http://www.dianping.com/search/category/1/10/g101r801'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
flag = 0

while (url != None):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    # 餐厅总数
    Sum = soup.find(attrs={'class': 'num'}).string
    # 餐厅名称
    names = soup.find_all('a', attrs={'data-hippo-type': 'shop'})
    # 星级
    levels = soup.find_all(['span'], attrs={'class': re.compile(r"sml-rank-stars(\s\w+)?")})
    # 评论数
    nums = soup.find_all('a', attrs={'class': 'review-num'})
    # 人均消费
    prices = soup.find_all('a', attrs={'class': 'mean-price'})
    # 菜系区域
    caixis = soup.select('div[class="tag-addr"] a')
    # 详细地址
    addrs = soup.find_all('span', attrs={'class': 'addr'})
    # 口味、环境、服务评分
    comments = soup.find_all('span', attrs={'class': 'comment-list'})
    if (flag == 0):
        info = 'Sum: ' + str(Sum).replace('(', '').replace(')', '') + '\n' + '#########################################'

    for (a, b, c, d, e, f, g) in zip(names, levels, nums, prices, caixis, addrs, comments):
        info = info + '\n' + 'name: ' + str(a.text.encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'level: ' + str(b.get('title').encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'num: ' + str(c.text.encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'price: ' + str(d.text.encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'caixi: ' + str(e.text.encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'addr: ' + str(f.text.encode('gb18030').replace(' ', ''))
        info = info + '\n' + 'comment: ' + str(g.text.encode('gb18030').replace(' ', ''))
        info += '\n' + '#########################################'

    file = open('result.txt', 'a')
    file = file.write(info)

    info = ''
    flag = 1

    url = soup.find('a', attrs={'class': 'next', 'title': '下一页'})
    if (url != None):
        url = url.get('href')
        url = base_url + str(url)

print("end")
