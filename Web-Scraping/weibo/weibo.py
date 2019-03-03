import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring,tostring


def get_html():

    url='http://www.ttmeiwen.com'
    r=requests.get(url)
    r=r.text
    #print(r)
    soup=BeautifulSoup(r,'html.parser')
    s=soup.find_all('ul',attrs={'class': 'list-unstyled'})
    s = repr(s[0])
    tree = fromstring(s)
    s = tostring(tree, pretty_print=True)
    soup = BeautifulSoup(s, 'html.parser')
    s=soup.find_all('li')
    s=repr(s[0])
    #print(s)
    s = tostring(tree, pretty_print=True)
    soup = BeautifulSoup(s, 'html.parser')
    s = soup.find_all('a')
    t=soup.find_all('a',attrs={'class':'title pull-left'})
    s = repr(s[2])
    t=repr(t[0])
    r1='[a-zA-z]+://[^\s]+html'
    r2='[\u4e00-\u9fa5].+[\u4e00-\u9fa5]'
    url=re.findall(r1,s)
    title=re.findall(r2,s)
    t=re.findall(r2,t)
    print(t[0])
    title=title[0].split('。')
    #print(title)
    l=title[0]
    print(l)
    print(url[0])

def int():
    get_html()

int()