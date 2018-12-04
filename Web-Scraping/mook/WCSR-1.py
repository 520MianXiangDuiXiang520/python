import requests
r=requests.get("https://www.baidu.com/robots.txt")
#返回状态吗
print(r.status_code)
#查看编码方式
print(r.encoding)
print(r.text[:1000])
f=open('E:\桌面文件\py\py-1','a')
f.write(r.text[:1000])