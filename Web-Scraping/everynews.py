
import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring,tostring


def get_wz():
    try:
        headers = {
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

        url='https://github.com/explore'
        github_url='https://github.com'
        r=requests.get(url,headers=headers)
        r=r.text
        soup=BeautifulSoup(r,'html.parser')
        s=soup.find('article',attrs={'class':'Story col-6 col-sm-4'})
        s=repr(s)
        tree = fromstring(s)
        s = tostring(tree, pretty_print=True)
        soup = BeautifulSoup(s, 'html.parser')
        url = soup.find_all('a',attrs={'data-ga-click':'Repository, go to repository'})
        miaoshu=soup.find_all('div',attrs={'class':'text-gray mb-2 ws-normal'})
        star=soup.find_all('a',attrs={'class':'d-inline-block link-gray mr-4'})
        num=soup.find_all('a', attrs={'class': 'd-inline-block link-gray mr-4'})
        print(num[0])
        link=[]
        stars=[]
        for href in url:
            link.append(href.get('href'))
        for st in star:
            stars.append(st.get('href'))
        r1='>.+<'
        r2='([1-9]\d*\.\d*|0\.\d*[1-9]\d*)k'
        title=re.findall(r1,repr(miaoshu[0]))
        star_num=re.findall(r2,repr(num[0]))
        branch_num = re.findall(r2, repr(num[1]))
        url=github_url+link[0]
        star_url=github_url+stars[0]
        branch_url=github_url+stars[1]
        info={'titlt':title[0],'url':url,'star_num':star_num,'star_url':star_url,'branch_num':branch_num,'branch_url':branch_url}
        print(info)
    except:
        info = {'titlt': '爬虫走丢了'}
        print(info)

if __name__ == '__main__':
    get_wz()