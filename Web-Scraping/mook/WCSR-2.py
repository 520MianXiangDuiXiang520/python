import requests
url="http://datsec.taropowder.cn/blog/33/?direction=sec"
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
    f = open('E:\桌面文件\py\py-2', 'a')
    f.write(r.text[:1000])
except:
    print("爬取失败")
