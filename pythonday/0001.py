# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**
# （或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# Python3中String模块ascii_letters和digits方法，其中ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9.
# ascii_uppercase大写字母
# ascii_downpercase小写字母
# python 随机函数random 注意，产出的不是真正的随机数，random随机数由随机种子经过梅森旋转算法产生，只要随机种子给定
# 产生的随机数就是唯一确定的，随机种子random.seed()设置，默认为系统时间，精确到毫秒
# https://www.jb51.net/article/130368.htm

import random,string
def vip(length):
    vipstr=''
    dir=string.ascii_uppercase+string.digits
    for i in range(length):
        t=random.choice(dir)
        vipstr=vipstr+t
    print(vipstr)
    file=open('0001.txt','a')
    file.write(vipstr+'\n')

def main(num,length):
    for i in range(num):
        vip(length)

main(200,20)