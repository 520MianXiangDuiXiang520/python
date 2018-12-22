# xlsx 文件读写
import json
from openpyxl import Workbook

def dic():
    D=open('0013','r',encoding='UTF-8')
    txt=D.read()
    tex=json.loads(txt)
    key=tex.keys()
    key=list(key)
    workbook=Workbook()
    booksheet=workbook.active
    for i in range(1,len(tex)+1):
        booksheet.append([key[i-1], tex[key[i-1]][0],tex[key[i-1]][1],tex[key[i-1]][2],tex[key[i-1]][3]])
    workbook.save('0013.xlsx')

if __name__ == '__main__':
    dic()
