import requests
#from bs4 import BeautifulSoup
#添加请求头伪装成浏览器
res=requests.get('http://bj.xiaozhu.com/')
#soup=BeautifulSoup(res.text,'html.parser')
#price=soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
#返回状态吗，200即为成功
print("状态吗：",res)
print(res.text )
#try:
    #print(soup.find('div'))
    #print(soup.select('#list_filter > div.city_l > div.clearfix.mb_14'))

    #print(price)
#except ConnectionError:
    #print("拒绝链接")
