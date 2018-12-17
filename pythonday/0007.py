#############################################
#  题目：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
#        包括空行和注释，但是要分别列出来。
#
#  思路：
#  1.遍历文件夹，判断文件后缀是否是.py
#  2.按行读取
#  3.判断是否是空行或者注释
#
###############################################

import os
import re

#遍历文件夹，以列表形式返回便利结果

def get_all_file(fill_path):
    fill_name=[]
    for filename in os.listdir(fill_path):
       fill_name.append(filename)
    return list(fill_name)

# 找出列表中的.py文件，以列表形式返回
# 使用正则表达式，由于re.match()是从字符串开始匹配，如果开头与表达式不匹配，返回NONE

def get_fill_py(fill_name):
    fill_py = []
    r1=r'.+.py$'
    for str in fill_name:
        p=re.match(r1,str)
        if(p):
             fill_py.append(p.group())
    return list(fill_py)

# 按行读取文件内容,把每一行以列表返回

def line(file_py):
    line=[]
    for file_name_one in fill_py:
        try:
            fo = open(path+"\\"+file_name_one , 'r',encoding='UTF-8')
             # readlines()以列表返回文件所有行
            for p in fo.readlines():
                line.append(p)
        except:
            continue
    return line

# 判断文件有多少行,注释

def line_num(line):
    line_number = len(line)
    zhushi_num=0
    huanhang=0
    r2=r'( )+#.+|#.+|( )+#'
    r3=r'(\n)|( )+\n'
    for zhushi in line:
        p=re.match(r2,zhushi)
        p_kong=re.match(r3,zhushi)
        if (p):
            zhushi_num=int(zhushi_num)+1
        elif(p_kong):
            huanhang=int(huanhang)+1
    return line_number,zhushi_num,huanhang

if __name__ == '__main__':
    global path
    path = 'E:\PYthon\pythonday\Web-Scraping\mook'
    global line_number
    line_number = 0
    fill_name = get_all_file(path)
    fill_py = get_fill_py(fill_name)
    lin = line(fill_py)
    num = line_num(lin)
    print('\n'+"在  "+path+"  目录下总共有"+repr(num[0])+"行代码，其中注释有"+repr(num[1])+"行，空行有"+repr(num[2])+"行")


