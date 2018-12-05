import requests
from bs4 import BeautifulSoup
import bs4
import re

url_stare='http://datsec.taropowder.cn/?page='
page=1
for i in range(5):
    p=repr(page)
    url=url_stare+p
    print(url)
    r=requests.get(url)
    demo=r.text
    r1=r'<a.+href="http.+</a>'
    href=re.findall(r1,demo)
    print(href)
    page=page+1

