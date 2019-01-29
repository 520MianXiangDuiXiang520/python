from urllib.request import urlopen,Request
from http.client import HTTPResponse

url='http://www.bing.com'
User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
req=Request(url,headers={'User-agent':User_Agent})
response=urlopen(req)
print(response.closed)

with response:
    print(type(response))
    print(response.status)
    # print(response._method)
    # print(response.read())
    print(response.geturl())
    print(response.info())

print(req.get_header('User-agent'))
print(response.closed)