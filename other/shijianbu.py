# 实践部渡心小栈推文顺序表
import calendar
name=['布嘉琪','张竞文','高天琦','王自愿','刘晓芳','耿梦琪','冯梦圆','宋逸飞','潘含沛','苏庆玲']
Noname=0
turn=[]
class people:
    def __init__(self):
        self.name=None
        self.month=-1
        self.day=-1
        self.week=''

class CroHeart(people):
    def __init__(self):
        super().__init__()
        self.startmon=4
    def getday(self):
        global Noname
        month=self.startmon
        day=15
        while month<=9:
            while day<=31:
                try:
                    week=calendar.weekday(2019,month,day)
                    if week==0 or week==4:
                        p1=people()
                        p1.name = name[Noname]
                        p1.day=day
                        p1.month=month
                        if week==0:
                            p1.week='星期一'
                        elif week==4:
                            p1.week='星期五'
                        turn.append(p1)
                        Noname += 1
                        if(Noname==10):
                            Noname=0

                    day+=1
                except:
                    day+=1
                    continue
            month+=1
            day=1

if __name__ == '__main__':
    cro=CroHeart()
    cro.getday()
    i=1
    with open('公众号.txt','a') as fp:
        for s in turn:
            print("%2d . 2019年%2d月%2d日，%s  ：%s"%(i,s.month,s.day,s.week,s.name))
            fp.write(("%2d . 2019年%2d月%2d日，%s  ：%s \n"%(i,s.month,s.day,s.week,s.name)))
            i+=1
        fp.close()



