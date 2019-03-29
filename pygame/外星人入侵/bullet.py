import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,setting,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_heigh)
        self.rect.top=ship.rect.top
        self.rect.centerx=ship.rect.centerx
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.color=setting.bullet_color
        self.speed=setting.bullet_speed_factor
        self.fire_type=ship.fire_type

    def update(self):
        if self.fire_type==2:
            self.x -= self.speed
            self.rect.x=self.x
        elif self.fire_type==1:
            self.x += self.speed
            self.rect.x = self.x
        elif self.fire_type==0:
            self.y-=self.speed
            self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
