import sqlite3

# 创建一个与数据库关联的Connection对象
conn=sqlite3.connect('boss/boss.db')
# 创建Cursor对象
cur=conn.cursor()
# 使用execute方法执行SQL语句
# cur.execute('''CREATE TABLE tests(date text,trans text)''')
# cur.execute('''INSERT INTO tests VALUES ('2019-4-1','SQLite')''')
for i in cur.execute('SELECT DISTINCT * FROM boss '):
    print(i)

# 保存修改
conn.commit()
# 关闭连接
conn.close()