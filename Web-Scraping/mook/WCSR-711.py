import requests
#from bs4 import BeautifulSoup
#import bs4
#调用正则表达式库
import re
page=1
#循环爬取七页内容
for i in range(7):
    url_stare = 'http://datsec.taropowder.cn/?page='
    #异常处理，出现异常，跳出本次循环
    try:
        #页数转换为字符串
        p=repr(page)
        #拼接url
        url=url_stare+p
        #用get方法爬取
        r=requests.get(url)
        #把爬取到的源码赋值给demo
        demo=r.text
        #使用正则表达式初步过滤出链接相关的信息
        r1=r'<a.+href="http.+</a>'
        href=re.findall(r1,demo)
        #循环对href列表中的所有值用正则表达式处理
        for j in range(len(href)):
            #link=href[j].split('"')
            #print(link[1],link[6])
            r2=r'http.+?"'
            r3=r'>.+?<'
            #用来过滤掉a标签中的类型等信息
            link=re.findall(r2,href[j])
            name=re.findall(r3,href[j])
            link=link[0]
            link=link.replace('"',' ')
            name=name[0]
            name=name.replace('>',' ')
            name = name.replace('<', ' ')
            #写入到文件
            f=open('711.txt','a+')
            f.write(link)
            f.write(name)
            f.write('\n')
            print(link,name)
        page=page+1
    except:
        continue


