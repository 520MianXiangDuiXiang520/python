import pygame

class Alien():
    def __init__(self,screen,setting):
        self.screen=screen
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.top=self.screen_rect.top
        self.speed=setting.alien_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)