import requests


url='https://fanyi.baidu.com/v2transapi'
header={
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '171',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BIDUPSID=B0A99125636D3EFB16FD1358E0CCD511; PSTM=1553156506; BAIDUID=4F4A20B467F0462BBD93B3CEBC2A7F25:FG=1; BDUSS=XVqblZWcHpnQVczemVrVU5mNDg3OGhXSEVKenRNQnJPVlNKSG9IeDJUelhBTU5jQVFBQUFBJCQAAAAAAAAAAAEAAAABt~0m1cW-~bGjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANdzm1zXc5tcd; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; pgv_pvi=2567291904; locale=zh; DOUBLE_LANG_SWITCH=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1556268001,1556268189,1556288483,1556288503; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1556288503; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
'Host': 'fanyi.baidu.com',
'Origin': 'https://fanyi.baidu.com',
'Referer': 'https://fanyi.baidu.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}

data={
'from': 'en',
'to': 'zh',
'query': 'hello',
'transtype': 'translang',
'simple_means_flag': 3,
'sign': 54706.276099,
'token': '34cd1560b436810d8ed95034d10ab2a0',
}

res=requests.post(url,headers=header,data=data)
print(res.text.encode())
