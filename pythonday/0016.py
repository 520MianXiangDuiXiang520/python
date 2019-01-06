# 老式挂钟会在整点的报时，响铃的次数和时间相等。我们设计一个在电脑上运行的报时器。
# 功能描述：运行后，在每一个整点长响一声，半个整点短响两声。实现睡眠模式，晚上十二点到早上六点不响铃。

import time
import pygame

def gettime():
    目前时间=time.localtime()
    # 目前时间=time.strftime("%Y-%m-%d %H:%M:%S",目前时间 )
    目前分钟 = time.strftime("%M", 目前时间)
    return 目前分钟

def playmusic(path,歌长):
    pygame.mixer.init()   # 初始化音频部分
    pygame.mixer.music.load(path)   # 载入音乐
    pygame.mixer.music.play()   # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
    time.sleep(歌长)   # 延时一定的时间，等待播放完再停止
    pygame.mixer.music.stop()   # 停止播放


if __name__ == '__main__':
    file1 = r'E:\PYthon\pythonday\pythonday\0016\山间清晨.wav'
    file2 = r'E:\PYthon\pythonday\pythonday\0016\百灵鸟音效.wav'
    while(1):
        分钟=gettime()
        if (分钟 == '30'):
            歌长=28
            playmusic(file1,歌长)
            time.sleep(60 - 歌长)
        if(分钟=='00'):
            歌长 = 5
            playmusic(file2,歌长)
            time.sleep(60 - 歌长)
