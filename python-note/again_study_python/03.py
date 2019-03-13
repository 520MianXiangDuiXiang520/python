flag=True
while flag:
    pl=input("请输入配料：")
    if pl=="exit":
        flag=False
    else:
        print("%s 将被加入到披萨中" % pl)