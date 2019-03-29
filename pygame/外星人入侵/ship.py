import pygame

class Ship():
    def __init__(self,screen,setting):
        self.screen=screen
        self.imag=pygame.image.load('images/ship.bmp')
        self.rect=self.imag.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed=setting.ship_speed_factor
        self.fire_type=0

    def blitme(self):
        self.screen.blit(self.imag,self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.speed
        elif self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx -= self.speed
        elif self.moving_up and self.rect.top>self.screen_rect.top:
            self.rect.centery -= self.speed
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery += self.speed
        elif self.rect.left==self.screen_rect.left:
            # 向右射击
            self.fire_type=1
        elif self.rect.right==self.screen_rect.right:
            # 向左射击
            self.fire_type = 2
