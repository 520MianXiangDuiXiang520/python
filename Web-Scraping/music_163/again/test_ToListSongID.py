import requests
from bs4 import BeautifulSoup
from Headers import Header
from Toplist import GetTopList
import sys
import io
class Test_TLSI:
    def __init__(self):
        self.url='https://music.163.com/discover/toplist?id=19723756'
        self.sour=requests.get(self.url)
        try:
            print(self.sour.text)
        except:
            pass

if __name__ == '__main__':


    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    s=Test_TLSI()
    print('\xb2\xbb\xb8\xd0\xd0\xcb\xc8\xa4')