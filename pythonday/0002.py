#将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

#先把0001的代码复制过来（‘_' )
import random,string
import pymysql
def vip(length):
    vipstr=''
    dir=string.ascii_uppercase+string.digits
    for i in range(length):
        t=random.choice(dir)
        vipstr=vipstr+t
    print(vipstr)
    mysql(vipstr)
    return vipstr

def main(num,length):
    for i in range(num):
        vip(length)

def mysql(vipst):
    # 打开数据库连接
    try:
        db = pymysql.connect("localhost", "root", "1234567", "pythonday")
    # 使用cursor()方法获取操作游标
        cursor = db.cursor()
    except:
        print("!!!!!")
    try:
        cursor.execute('USE pythonday;')
        db.commit()
    except:
        print("eeeee")
    try:
        # 执行sql语句
        cursor.execute('INSERT INTO day0002(vipnum) VALUES(%s)', (vipst))
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        print("error!")
        db.rollback()

main(200,20)