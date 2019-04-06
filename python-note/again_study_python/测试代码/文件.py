import pickle

class File:
    def pic(self):
        with open('文件.txt','r') as txtfp,open('文件.dat','wb') as datfp:
            lines=txtfp.readlines()
            # 把长度写入到第一位
            pickle.dump(len(lines), datfp)
            for line in lines:
                pickle.dump(line,datfp)

        with open('文件.dat','rb') as fp:
            n=pickle.load(fp)
            for f in range(n):
                print(pickle.load(fp))

f=File()
