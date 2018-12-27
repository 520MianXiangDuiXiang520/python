# 抓了a,b,c,d四名犯罪嫌疑人，其中有一人是小偷，审讯中：
# a说我不是小偷；
# b说c是小偷；
# c说小偷肯定是d；
# d说c胡说！
# 其中有三个人说的是实话，一个人说的是假话，请编程推断谁是小偷
# 1代表是小偷，0代表不是小偷。

# 方法一： 群举法
s=0
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if(a+b+c+d==1):
                    if(a==0 ):
                        s += 1;
                    if(c==1):
                        s += 1;
                    if(b==0 or b==1):
                        s+=1;
                    if( s==3):
                        if(a==1):
                            print("a is Thief")
                        elif(b==1):
                            print("b is Thief")
                        elif(c==1):
                            print("c is Thief")
                        else:
                            print("d is Thief")
                        break
                    s=0;

# 方法二： 逻辑法

t=['A','B','C','D'];
for thief in t:
    sum=(thief!="A")+(thief=="C")+(thief=="D")+(thief!="D")
    if(sum==3):
        print(thief+" is Thief")
        break