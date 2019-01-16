import time
import pygame,sys
pygame.init()   # 初始化
size=width,height=600,400
screen=pygame.display.set_mode(size,pygame.RESIZABLE)   # 绘制窗口，允许调节大小
# Vinfo=pygame.display.Info()
#size=width,heught=Vinfo.current_w,Vinfo.current_h
BLUE = (0, 0, 128)   # 定义颜色
GREEN = (0, 255, 0)
Hour=0   # 时
minu=0   # 分
seco=0   # 秒
suspend=2   # 暂停
pygame.display.set_caption("真实 摁Esc暂停")   # 标题
while True:
    for event in pygame.event.get():   # 获得用户响应
        if event.type==pygame.QUIT:   # 退出
            sys.exit()
        elif event.type==pygame.KEYDOWN:   # 键盘
            if event.key==pygame.K_ESCAPE:   # Esc暂停
                suspend += 1
        elif event.type==pygame.VIDEORESIZE:   # 调整窗口大小时做出反应
            size = width, height = event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)
    font = pygame.font.Font("font/BAUHS93.TTF", 70)   # 字体
    f1rect = font.render(repr(Hour)+':'+repr(minu)+':'+repr(seco), True, GREEN)   # 输出内容
    textRech = f1rect.get_rect()
    textRech.center = (width/2, height/2)   # 输出位置
    screen.blit(f1rect, textRech)   # 输出
    pygame.display.update()   # 更新画面
    time.sleep(1)   # 延时
    if(suspend%2==0):   # 暂停
        seco += 1
    if (seco==60):   # 计时器
        seco=0
        minu+=1
    if minu==60:
        minu=0
        Hour+=1
    screen.fill((0, 0, 0))   # 覆盖


