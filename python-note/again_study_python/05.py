a=[2,4,6,8]
b=[1,3,5,7]
i=0
while True:
    i=input("请输入一个个位数：")
    i=int(i)
    if i in a:
        print("%d in list_a" % i)
    elif i not in a and i in b:
        print("%d not in list_a but in list_b" % i)
    else:
        print("%d not in a and not in b")
        break