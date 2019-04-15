# 作为导入模块
class Test:
    def __init__(self):
        print('执行导入模块init方法')
    def t(self):
        print('执行导入模块自定义方法')

if __name__ == '__main__':
    t=Test()
    print('执行导入模%s块main'%__name__)
    t.t()