#功能：使用递归实现汉诺塔
count=0
def honai(num,left,right,mid):
    global count
    if num==1:
        print("{}:{}->{}".format(1,left,right))
        count+=1
    else:
        honai(num-1,left,mid,right) 
