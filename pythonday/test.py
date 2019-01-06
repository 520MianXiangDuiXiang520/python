import time
import pygame
file=r'E:\PYthon\pythonday\pythonday\0016\嘟嘟嘟嘟嘟滴-整点报时音效.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()
