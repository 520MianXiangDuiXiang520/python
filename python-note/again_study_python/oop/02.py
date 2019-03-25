class HomeItem:
    name=''
    size=0
    def __init__(self,name,size):
        self.name=name
        self.size=size
        print("这是 %s 占地 %d " % (self.name,self.size))
    def __str__(self):
        return "这是 %s 占地 %d " % (self.name,self.size)

class HomeType:
    name=''
    size=0
    def __init__(self,type_name,type_size):
        self.name=type_name
        self.size=type_size


class Home():
    def __init__(self,home_type,ower):
        self.home_type=home_type
        self.ower=ower
        self.all_size=home_type.size
        self.rest_size=self.all_size
        self.item_list=[]

    def add_item(self,item_name):
        self.rest_size -= item_name.size
        if self.rest_size>0:
            self.item_list.append(item_name.name)
            print(self.item_list)
            print("剩余空间： %d " % self.rest_size)
        else:
            print("空间不足！剩下的加不了")

席梦思=HomeItem('席梦思',30)
电冰箱=HomeItem('电冰箱',20)
沙发=HomeItem('沙发',50)
豪华户型=HomeType('豪华户型',500)
普通户型=HomeType('普通户型',95)
小明家=Home(普通户型,'小明')
小明家.add_item(席梦思)
小明家.add_item(电冰箱)
小明家.add_item(沙发)

