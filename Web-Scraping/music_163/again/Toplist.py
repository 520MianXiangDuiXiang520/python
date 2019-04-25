# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring,tostring
from Headers import Header

class GetTopList:
    """
    get toplist url
    """
    def __init__(self):
        self._nameList=[]
        self._linkList=[]
        self.topdict={}
        self._rooturl='https://music.163.com'
        self._baseurl='https://music.163.com/discover/toplist'
        self._headers=Header.geth1()
        self._request=requests.get(self._baseurl,headers=self._headers)
        self._soup=BeautifulSoup(self._request.text,'html.parser')
        self._TopList=self._soup.find_all('a',attrs={'class':'s-fc0'})
        for l in self._TopList:
            name=l.text
            link=self._rooturl+l['href']
            self._linkList.append(link)
            self._nameList.append(name)



    def puturl(self):
        self.topdict=dict(zip(self._nameList[:24],self._linkList[:24]))
        return self.topdict



if __name__ == '__main__':
    s=GetTopList()
