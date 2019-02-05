# 首先打算爬取到歌手以及作评的id

import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import xlwt

global hang
global lie
hang=0
lie=0

def get_artists(url):
    global hang
    global lie
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
                         '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
                         'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
                         ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
                         'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
                         '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
                         '.1527319890.2; __utmb=94650624.3.10.1527319890',
               'Host': 'music.163.com',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    r=requests.get(url,headers=headers)
    text=r.text
    soup = BeautifulSoup(text, 'lxml')
    s=soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    r='[1-9]+.+的'
    id_r='([0-9]+[0-9])'
    art_r='[0-9]+" title="'
    art_r2='的'

    for i in s:
        #print(i)
        i=repr(i)
        ss=re.findall(r,i)
        #print(type(i))
        #print(type(ss))
        ids=re.findall(id_r,ss[0])
        #arts=re.findall(art_r,repr(ss))
        arts=re.sub(art_r,"",ss[0])
        arts = re.sub(art_r2, "", arts)
        id.append(ids[0])
        artists.append(repr(arts))

if __name__ == '__main__':
    id=[1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    dir={
        '1001':'华语男歌手',
        '1002':'华语女歌手',
        '1003': '华语组合乐队',
        '2001': '欧美男歌手',
        '2002': '欧美女歌手',
        '2003': '欧美组合乐队',
        '6001': '日本男歌手',
        '6002': '日本女歌手',
        '6003':'日本组合乐队',
        '7001': '韩国男歌手',
        '7002': '韩国女歌手',
        '7003': '韩国组合乐队',
        '4001': '其他男歌手',
        '4002': '其他女歌手',
        '4003': '其他女歌手',
    }
    initial=[-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    for ii in id:
        artists = []
        id = []
        for jj in initial:
            url='https://music.163.com/discover/artist/cat?id='+repr(ii)+'&initial='+repr(jj)
            get_artists(url)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        worksheet = workbook.add_sheet('歌手')
        # 写入excel
        # 参数对应 行, 列, 值
        for i in range(len(id)):
            worksheet.write(i, 0, label=id[i])
            #hang=hang+1
        for j in range(len(artists)):
            worksheet.write(j,1, label=artists[j])
            #lie=lie+1

        name=dir[repr(ii)]+'.xls'
        # 保存
        workbook.save(name)




