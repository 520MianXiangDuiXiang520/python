import requests
from bs4 import BeautifulSoup
from retrying import retry

@retry(stop_max_attempt_number=5)
def test():

    url='http://127.0.0.1:8000/auth/login/'
    url_home='http://127.0.0.1:8000/auth/home/'

    headers={
        'Cookie':'sessionid = jxvbtbrfl8jti6f5britml6whxwrqjvi'
    }
    request=requests.get(url,timeout=5)
    p=requests.get(url_home,headers=headers)
    print(p.text)
    soup=BeautifulSoup(request.text,'html.parser')
    csrf_value=soup.find('input',attrs={'name':'csrfmiddlewaretoken'})['value']
    # print(csrf_value)
    # print(request.text)
    data={
    'csrfmiddlewaretoken': csrf_value,
    '用户名': '123456789',
    '密码': 'zjb19990805'
    }
    session=requests.session()
    session.post(url,data=data)
    s=session.get(url_home)
    with open('login.html','w',encoding='utf-8') as fp:
        fp.write(s.text)
    print(s.text)

test()