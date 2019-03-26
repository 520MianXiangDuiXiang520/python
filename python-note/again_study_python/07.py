def input_psw():
    psw=input("请输入密码： ")
    if len(psw)<8:
        error=Exception("密码长度不够")
        raise error
    else:
        return psw
try:
    s=input_psw()
except Exception as error:
    print(error)
else:
    print(s)
finally:
    print("---end---")