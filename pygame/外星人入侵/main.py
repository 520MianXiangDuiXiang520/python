import sys
import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_function as gf
from alien import Alien

def run_game():
    pygame.init()
    screen=pygame.display.set_mode(Settings().size)
    pygame.display.set_caption('外星人入侵')
    ship=Ship(screen,Settings())
    alien=Alien(screen,Settings())
    bullets=Group()
    aliens=Group()
    while True:
        gf.check_events(ship,Settings(),screen,bullets)
        gf.create_alien(Settings(),screen,aliens)
        gf.update_bullet(bullets,Settings())
        gf.update_screen(Settings(),screen,ship,bullets,alien)



if __name__ == '__main__':
    run_game()