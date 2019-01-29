import urllib.request
import urllib.parse

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data={}
data['i']='我'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15487543807487'
data['sign']='a7df7827fcb04f56f53f01c8161acb87'
data['ts']='1548754380748'
data['bv']='363eb5a1de8cfbadd0cd78bd6bd43bee'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'
data=urllib.parse.urlencode(data).encode('UTF-8')
request=urllib.request.urlopen(url,data)
html=request.read().decode('UTF-8')
print(request.getcode())
print(html)

