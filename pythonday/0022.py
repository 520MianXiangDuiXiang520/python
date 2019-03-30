import math
class PI:
    pi = ''
    def __init__(self,filename):
        with open(filename) as fill:
            lines=fill.readlines()
        for line in lines:
            PI.pi+=line.strip('\n')

    def birth_in(self,birth):
        '''判断输入的生日是否在PI内'''
        result=PI.pi.find(birth)
        num=PI.pi.count(birth)
        first_find=PI.pi.index(birth)
        if result==-1:
            print("不在")
        else:
            print('您的生日在圆周率前1000000位中出现 %d 次' % num)
            print("第一次出现在 %d 到 %d 位" % (first_find,first_find+len(birth)))

    def statistics(self):
        '''统计每个数字出现的次数'''
        stat=[0,0,0,0,0,0,0,0,0,0]
        id=0
        for i in range(len(PI.pi)):
            if PI.pi[i]=='.':
                continue
            s=int(PI.pi[i])
            stat[s]+=1

        for i in stat:
            long=(i-99000)/20
            print(repr(id)+" : "+'@'*math.ceil(long)+"  ("+repr(i)+"次)")
            id += 1
    def jiou(self,num):
        print(PI.pi[int(num)])

    def info(self):
        print(len(PI.pi))
        #print(PI.pi[6956])
        print(PI.pi)

if __name__ == '__main__':
    p=PI('0022.txt')

    # try:
    #     birth = input("按20190203的格式输入生日：\n")
    #     p.birth_in(birth)
    # except ValueError:
    #     print("没有找到")
    #
    # p.statistics()
    num=input("find n ?")
    p.jiou(num)
