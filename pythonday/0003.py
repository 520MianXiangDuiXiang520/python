import re
r1=r'([a-zA-Z-]+)'
file=open('little king','r',encoding='UTF-8')
pp=file.read()
list=re.findall(r1,pp)
#print(list)
num=len(list)
print('小王子全文 '+repr(num)+" 字")


# 1.findall返回所有符合正则表达式的值到列表中
# 2. repr()将其他类型强制转换为字符串类型，类似有如下：
#   int(x [,base]) ⇒ 将x转换为一个十进制的整数
#   long(x [,base]) ⇒ 将x转换为一个十进制的长整数
#   float(x) ⇒ 将x转换为一个浮点数
#   str(object) ⇒ 转换为字符串
#   repr(object) ⇒ 转换为表达式字符串
#   eval(str) ⇒ 用来计算在字符串中的有效Python表达式,并返回一个对象
#   tuple(seq) ⇒ 将序列seq转换为一个元组
#   list(seq) ⇒ 将序列seq转换为一个列表
#   chr(x ) ⇒ 将一个整数转换为一个字符
#   unichr(x ) ⇒ 将一个整数转换为Unicode字符
#   ord(x ) ⇒ 将一个字符转换为它的整数值
#   hex(x ) ⇒ 将一个整数转换为一个十六进制字符串
#   oct(x ) ⇒ 将一个整数转换为一个八进制字符串
# 3.re包：
#       compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
#       扫描整个字符串并返回第一个成功的匹配。函数语法：re.search(pattern, string, flags=0)
#       findall()找到 RE 匹配的所有子串，并把它们作为一个列表返回
#       split()将字符串在 RE 匹配的地方分片并生成一个列表
#
#