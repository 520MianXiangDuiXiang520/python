# 你有一个HTML页面，找出他的正文和链接
import requests
from bs4 import BeautifulSoup
# 获取HTML页面
def getHtml(URL):
    p=requests.get(URL)
    html=p.text
    return html

# 找出正文,链接
def getBody(html):
    soup=BeautifulSoup(html,'html.parser')
    body=soup.find_all('body')
    link=soup.find_all('a')
    print(body)
    print(link)


if __name__ == '__main__':
    URL = "http://datsec.taropowder.cn/blog/33/"
    html = getHtml(URL)
    getBody(html)