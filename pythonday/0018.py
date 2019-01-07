import time
import pygame,sys
pygame.init()
size=width,height=600,400
screen=pygame.display.set_mode(size,pygame.RESIZABLE)
Vinfo=pygame.display.Info()
#size=width,heught=Vinfo.current_w,Vinfo.current_h
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
Hour=0
minu=0
seco=0
suspend=2
pygame.display.set_caption("真实 摁Esc暂停")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                suspend += 1
        elif event.type==pygame.VIDEORESIZE:
            size = width, height = event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)
    font = pygame.font.Font("font/BAUHS93.TTF", 70)
    f1rect = font.render(repr(Hour)+':'+repr(minu)+':'+repr(seco), True, GREEN)
    textRech = f1rect.get_rect()
    textRech.center = (width/2, height/2)
    screen.blit(f1rect, textRech)
    pygame.display.update()
    time.sleep(1)
    if(suspend%2==0):
        seco += 1
    if (seco==60):
        seco=0
        minu+=1
    if minu==60:
        minu=0
        Hour+=1
    screen.fill((0, 0, 0))


