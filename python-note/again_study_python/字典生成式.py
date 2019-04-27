header='''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: _ga=GA1.2.1934859142.1553158342; __gads=ID=bb2c52e7f95e20ea:T=1553158342:S=ALNI_MbCqantLKdwLUa38oG6ZMcHeLfCjA; sc_is_visitor_unique=rx9614694.1553935711.DBD9700252C94FAFBCEA644716871ED5.1.1.1.1.1.1.1.1.1; UM_distinctid=169d2216183388-07ae2582475b69-7a1437-144000-169d2216184432; CNZZDATA1260206164=1990517475-1554008597-https%253A%252F%252Fwww.baidu.com%252F%7C1554008597; _gid=GA1.2.1584687891.1556348763; __utmz=226521935.1556352396.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=226521935.1934859142.1553158342.1556352396.1556352395.1
if-modified-since: Sat, 27 Apr 2019 13:11:17 GMT
referer: https://www.google.com/
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'''
print(type(header))
header={i.split(":")[0]:i.split(":")[1] for i in header.split('\n')}
print(header)
s={'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
   'accept-encoding': ' gzip, deflate, br',
   'accept-language': ' zh-CN,zh;q=0.9',
   'cache-control': ' max-age=0',
   'cookie': ' _ga=GA1.2.1934859142.1553158342; __gads=ID=bb2c52e7f95e20ea',
   'if-modified-since': ' Sat, 27 Apr 2019 13',
   'referer': ' https',
   'upgrade-insecure-requests': ' 1',
   'user-agent': ' Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36'
   }
