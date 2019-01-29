import urllib.request

req=urllib.request.Request('http://placekitten.com/201/300')
print(req)
request=urllib.request.urlopen(req)

# request.info() 返回URL头部信息
print(request.info())

# request.getcode() 返回响应状态码
print(request.getcode())

#request.geturl() 返回实际访问的网址，如果网址有重定向，会返回重定向后的网址
print(request.geturl())

cat_img=request.read()

with open('cat/cat0.jpg','wb') as f:
    f.write(cat_img)

