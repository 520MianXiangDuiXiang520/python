l=[1,2,3,'4',5.0]
print("初始",l)
l[4]=8
l.append(4.0)
l.insert(2,'9.k')
l.pop(1)
print(l)
t=(1,2,['a','b'])
print(t[2])
t[2][1]=['b','a']
print(t)
d={
    'wuzhipeng':12345,
    'geqiangshen':23456,
    'mayun':89765
}
print(d['wuzhipeng'])
d['wuzhipeng']=45678
print(d['wuzhipeng'])
for i in d:
    print(i,":",d[i])
s=set([1,2,3,4])
print(s)
s.add('5')
print(s)
s.remove(3)
print(s)
i='z'
s=set(['a','b','c','d'])
if i in s:
    print("ok")
else:
    print("error")