#百度关键字搜索接口：www.baidu.com/s?wd=keyword
#360关键字搜索接口：www.so.com/s?q=keyword
import requests
keyword="python"
url="http://www.baidu.com/s"
head={'user-agent':'Mozilla/5.0'}
try:
    kv={'wd':keyword}
    r=requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(len(r.text))
    f = open('E:\桌面文件\py\py-4.txt', 'a')
    f.write(r.text[1000:2000])
except:
    print("爬取失败")
