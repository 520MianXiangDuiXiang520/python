class 列表生成式练习:
    def 数组平铺(self):
        a = [[a for a in range(3)]] * 3
        print(a)
        s = [j for i in a for j in i]
        print(s)
    def 等差数列(self,begin,num):
        l=[begin+11*a for a in range(num) ]
        print(l)
    def 成绩最好(self):
        dir={'zhangsan':95,'lisi':59,'wangwu':78,'zhaoliu':87,'xiaohua':100}
        max_score=max(dir.values())
        max_name=[max_name for max_name in dir if dir[max_name]==max_score]
        print(max_name)
    def 矩阵转置(self):
        l=[[1,2,3],[4,5,6],[7,8,9]]
        s=[[r[i] for r in l] for i in range(3)]
        print(s)


if __name__ == '__main__':
    li=列表生成式练习()
    # li.等差数列(0,10)
    # li.成绩最好()
    li.矩阵转置()