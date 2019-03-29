import pygame
import sys
from bullet import Bullet
from alien import Alien

def fire_bullet(ship,setting,screen,bullets):
    if len(bullets) < setting.bullet_maxcount:
        new_bullet = Bullet(screen, setting, ship)
        bullets.add(new_bullet)

def create_alien(setting,screen,aliens):
    for i in range(setting.alien_count):
        new_alien=Alien(screen,setting)
        aliens.add(new_alien)

def check_events_KeyDown(ship,event,setting,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ship,setting,screen,bullets)


def check_events_KeyUp(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship,setting,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_events_KeyDown(ship,event,setting,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_events_KeyUp(ship,event)

def update_screen(setting,screen,ship,bullets,aliens):
    screen.fill(setting.bg_color)
    ship.blitme()
    ship.update()
    for bullent,alien in bullets.sprites(),aliens.sprites():
        bullent.draw_bullet()
        bullent.update()
    pygame.display.flip()

def update_bullet(bullets,setting):
    for bullent in bullets.copy():
        if bullent.rect.bottom < 0 or bullent.rect.left<0 or bullent.rect.right>setting.width:
            bullets.remove(bullent)