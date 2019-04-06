from sys import argv
print(argv)
ar=argv
print(ar)


'''
argv用来接收命令行参数，使用命令行运行脚本时，后面的参数会被作为列表的值传入列表
argv[0]是脚本名，如在命令行中：

E:\PYthon\pythonday\python-note\again_study_python>python 06.py 1 2 3 4
['06.py', '1', '2', '3', '4']
['06.py', '1', '2', '3', '4']

'''