import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx=random.randint(10,int(setting.width-10))
        self.rect.top=random.randint(0,int(setting.heigh/4))
        self.y=float(self.rect.y)
        self.speed=setting.alien_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y=self.y
