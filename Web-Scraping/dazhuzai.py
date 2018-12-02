import requests
import re
import time
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64;) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/56.0.2924.87 Safri/537.36'}
header = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
f=open('e:/dazhuzai.txt','a+')
def get_info(url):
    res=requests.get(url,headers=header)
    if res.status_code==200:
        contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass

if __name__=='__main__':
    urls=['http://127.0.0.1/list.php'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()