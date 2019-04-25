from Toplist import GetTopList
from TopListSongID import SongID
from download import DownLoad


if __name__ == '__main__':

    type=int(input('请选择板块：'))
    if type==1:
        s = GetTopList()


        num=1
        print("*"*100)
        for i in s.puturl():
            print(repr(num)+":"+i)
            num+=1
        topno=input('选择板块：')
        num=1
        id_Dict = SongID(int(topno)-1).songid

        for i in id_Dict.values():
            print(repr(num)+":"+i)
            num+=1
        Choice_No=int(input('选择要下载的歌：'))
        ID=list(id_Dict.keys())[Choice_No-1]
        NAME=list(id_Dict.values())[Choice_No-1]
        path='E:/桌面文件/again'
        down = DownLoad(ID,NAME,path)


