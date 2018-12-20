# 字符串模式匹配，使用KMP快速匹配算法

# 读取文件内容，产生一个字符串

def getStr(path):
    str=""
    file=open(path,'r',encoding='UTF-8')
    str=file.read()
    str=repr(str)
    return str

# 获得KMP next数组

def getNext(strSeq,next):
    next.append(-1)
    i=0
    j=-1
    while(i<len(strSeq)):
        if(j==-1 or strSeq[i]==strSeq[j]):
            i += 1
            j += 1
            next.append(j)
        else:
            j=next[j]
    print(next)
    return next

# KMP 算法
def KMP (seqString,seq,next):
    i=0
    j=0
    while(i<len(seqString) and j<len(seq)):
        if(j==-1 or seqString[i]==seq[j]):
            i+=1
            j+=1
        else:
            j=next[j]
    if(j==len(str)):
        return i-len(str)
    else:
        return -1

if __name__ == '__main__':
    str="abab"
    seqstring="hhababj"
    next=[]
    next=getNext(str,next)
    s=KMP(seqstring,str,next)
    print(s)