import xlwt

file=open('0021.txt','r',encoding='utf-8')
s=file.read()
li=eval(s)
print(li[0][1])

workbook=xlwt.Workbook()
table=workbook.add_sheet('0021')
for i in range(len(li)):
    for j in range(len(li[i])):
        table.write(i,j,li[i][j])

workbook.save('0021.xls')