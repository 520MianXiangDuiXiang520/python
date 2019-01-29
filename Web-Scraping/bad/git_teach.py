import requests
from bs4 import BeautifulSoup
import re
headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'}
url='http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374027586935cf69c53637d8458c9aec27dd546a6cd6000'
r=requests.get(url,headers=headers)
demo=r.text
print(demo)
#soup=BeautifulSoup(demo,"html,parser")
#href=soup.find_all('a')
#print(href)