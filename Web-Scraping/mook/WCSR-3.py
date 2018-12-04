import requests
#模拟浏览器
head={'user-agent':'Mozilla/5.0'}
url="http://www.divcss5.com/cssrumen/"
try:
    r=requests.get(url,headers=head)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
    f = open('E:\桌面文件\py\py-3.txt', 'a')
    f.write(r.text[1000:2000])
except:
    print("爬取失败")