# 模拟凯斯加密算法
import string

lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
before=lowercase+uppercase
after=lowercase[2:]+lowercase[:2]+uppercase[2:]+uppercase[:2]
table=''.maketrans(before,after)
input=input("please input:")
kasa=input.translate(table)
print(kasa)