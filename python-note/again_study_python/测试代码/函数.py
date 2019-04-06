
def test(*args,**kwargs):
    """测试多值参数"""
    print(args)
    print(kwargs)

def test2(a,b,c):
    """测试解包"""
    print(a,b,c)

s=[]

def test4():
    return s.append(i**2)

def test3():
    for i in range(10):
        # s.append(lambda:i**2)
        s.append(i**2)



# test(1,2,3,4,name='dapeng',ages=20)

# test2(1,*(2,3))
# test2(*(2,3),1)
#
# test2(1,2,c=3)
# test2(c=3,*(1,2))

test3()
print(s[2])


