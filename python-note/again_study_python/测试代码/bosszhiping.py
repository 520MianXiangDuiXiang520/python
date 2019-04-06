import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.zhipin.com/c100010000/e_102/?query=python&page=2&ka=page-1'
headers={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'sid=sem; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1554520473; t=EhYzsWWdwhoHIYYh; wt=EhYzsWWdwhoHIYYh; JSESSIONID=""; __c=1554520518; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26utm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_campaign%3DPC-yixian-pinpaici-2C%26utm_content%3DBOSSzhipin-rencai%26utm_term%3DBOSSzhipinrencaiwang&l=%2Fwww.zhipin.com%2Fgeek%2Fnew%2Findex%2Frecommend%3Frandom%3D1554520516885&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26utm_source%3Dbaidu%26utm_medium%3Dcpc%26utm_campaign%3DPC-yixian-pinpaici-2C%26utm_content%3DBOSSzhipin-rencai%26utm_term%3DBOSSzhipinrencaiw; _uab_collina=155452065630530987802467; __a=71084783.1554520472.1554520472.1554520518.27.2.26.27; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1554522323',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

r=requests.get(url,headers=headers)
text=r.text
soup=BeautifulSoup(text,'lxml')
ui=soup.find_all('div',attrs={'class':'job-primary'})
s=repr(ui[0])
soup_ui=BeautifulSoup(s,'html.parser')
title=soup_ui.find_all('div',attrs={'class':'job-title'})
red=soup_ui.find_all('span',attrs={'class':'red'})
p=soup_ui.find_all('p')
a=soup_ui.find_all('a')

title=repr(title[0])
red=repr(red[0])
address=repr(p[0])
num=repr(p[1])
url=repr(a[0])
fabu_date=repr(p[2])
title=re.sub('[\<].+?[\>]','',title)
red=re.sub('[\<].+?[\>]','',red)
add=re.sub('[\<].+?[\>]','',address)
num=re.sub('[\<].+?[\>]','',num)
num=re.findall('[0-9].+[人]',num)
date=re.sub('[\<].+?[\>]','',fabu_date)
url=re.findall("\/job_detail.+\.html",url)
url='https://www.zhipin.com'+url[0]

print(title)
print(red)
add=add.partition('应届生')
adds=add[0]
xueli=add[1]+add[2]
print(adds)
print(xueli)
print(num[0])
print(date)
print(url)