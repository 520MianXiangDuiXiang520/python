# 敏感词文本文件 0010.txt，里面的内容为以下内容，当用户输入敏感词语时，用*替换
# 试着用一下jieba库
import jieba

# 读取文件内容，保存到列表中

def getText(fillPath):
    line=[]
    file=open(fillPath,'r',encoding='UTF-8')
    for p in file.readlines():
        p = p.strip()
        jieba.add_word(p)
        line.append(p)
    return line

# 判断输入内容是否是敏感词语，是，输出*，不是，输出原来的语句
def out(getstr,list):
    lcut=jieba.lcut(getstr)
    s=""
    for l in lcut:
        for f in list:
            if l==f:
                l="*"
        s=s+l
    print(s)

if __name__ == '__main__':
    str=input("shuru")
    path='0010'
    out(str,getText(path))