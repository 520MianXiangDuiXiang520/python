import requests

class DownLoad:
    def __init__(self,id,name,path):
        self._id=id
        self._baseurl='http://music.163.com/song/media/outer/url?id='
        self.url=self._baseurl+str(self._id)
        try:
            e = requests.get(self.url.encode('utf-8'))
            print(e)
            with open(path + "/" + name + ".jpg", 'wb') as fp:
                fp.write(e.content)
                print(self.url.split('/')[-1] + '下载完成...')
                fp.close()
        except:
            print(self.url.split('/')[-1] + '爬取失败')