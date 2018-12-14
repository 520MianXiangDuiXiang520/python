#你有一个目录，放了你一个月的日记（我用了《星球大战》原文），都是 txt，为了避免分词的问题，假设内容都是英文，请统计出每篇日记中出现次数最多的词。
# 这道题关键在于遍历文件夹，我们使用os
import os
import re

 #  遍历文件夹，把所有文件名以列表形式返回

def get_all_file_name(file_path):
    file=[]
    for filename in os.listdir(file_path):
       file.append(filename)
    return list(file)

def openfile(filename):
    file=open(filename,'r')
    file_body=file.read()
    return file_body

def get_power_word(file_body):
    r1=r'([a-zA=Z-]+)'
    list=re.findall(r1,file_body)
    result = {}
    for i in set(list):
        result[i] = list.count(i)
    return result

def get_max_power_word(result):
    result=sorted(result.items(),key=lambda item:item[1],reverse=True)
    return result

def main():
    sq=get_all_file_name('0004 Star Wars')
    lenght=len(sq)
    for i in range(lenght):
        file_body=openfile('0004 Star Wars/'+sq[i])
        result=get_power_word(file_body)
        result=get_max_power_word(result)
        print(sq[i]+"中出现最多的四个词：",result[0],result[1],result[2],result[3])



main()