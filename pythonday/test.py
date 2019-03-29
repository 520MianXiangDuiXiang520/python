import json
list=[1,2,3,4,5,{"name":"home"}]
file_name='E:/桌面文件/test.json'
s=json.dumps(list)
print(type(s))
try:
    with open(file_name) as fileobject:
        r_js = json.load(fileobject)
        print(type(r_js))
        print(r_js)
except:
    with open(file_name, 'w') as fileobject:
        json.dump(list, fileobject)
