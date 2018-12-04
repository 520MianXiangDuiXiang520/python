import requests
from bs4 import BeautifulSoup
import bs4
def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#返回错误信息
        r.encoding=r.apparent_encoding#设置编码格式
        return r.text
    except:
        return ""
def fillUnivlist(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    #对源码中所有tbody标签孩子遍历，
    for tr in soup.find('tbody').children:
        #检测tr标签类型，不是Tag过滤
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivlist(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
def fileUnivlist(ulist,num):
    f = open('China-University-List.txt', 'w+')
    for i in range(num):
        f.write(ulist)
def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=gethtmltext(url)
    fillUnivlist(uinfo,html)
    printUnivlist(uinfo,300)
main()