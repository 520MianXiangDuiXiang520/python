from Headers import Header
from Toplist import GetTopList
import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring,tostring
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

class SongID(object):
    def __init__(self,No):
        l=GetTopList()
        self._urlNo=int(No)
        self._url=list(l.puturl().values())[self._urlNo]
        self.songid={}
        self._idlist=[]
        self._namelist=[]
        song_request = requests.get(self._url, headers=Header.geth2())
        song_div = (BeautifulSoup(song_request.text, 'html.parser')).find_all('div',attrs={'id': 'song-list-pre-cache'})
        s = BeautifulSoup(tostring(fromstring(repr(song_div[0])), pretty_print=True), 'html.parser').find_all('li')
        for i in s:
            href = BeautifulSoup(tostring(fromstring(repr(i)), pretty_print=True), 'html.parser').a['href']
            id=re.findall('[0-9].+',href)[0]
            self._idlist.append(id)
            name = BeautifulSoup(tostring(fromstring(repr(i)), pretty_print=True), 'html.parser').a.text
            self._namelist.append(name)
        self.songid=dict(zip(self._idlist,self._namelist))

            # print(href, name)

if __name__ == '__main__':

    g=SongID(13)
    print(g.songid )