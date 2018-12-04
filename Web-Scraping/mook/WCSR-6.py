import requests
from bs4 import BeautifulSoup
url="http://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#获得标签名称
print(soup.p)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
#获得标签属性
tag=soup.a
print(tag.attrs)
print(tag.attrs['href'])
print(soup.p.attrs)
#获得标签之间的内容
print(soup.p.string)
#格式化编码
print(soup.prettify())
#find_all(name[检索的标签名]，attrs[标签属性值的检索字符串，可标注属性检索]，recursive[是否对子孙全部检索，默认ture]，string[标签中字符串区域]，**kwargs)
print(soup.find_all('p','course',"ture"))