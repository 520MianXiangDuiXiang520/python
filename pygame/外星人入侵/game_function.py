import pygame
import sys
import time
import json
from bullet import Bullet
from alien import Alien


def fire_bullet(ship,setting,screen,bullets,stats):
    setting.bullet_maxcount += int(stats.score / 15)
    setting.bullet_speed_factor += int(stats.score / 15)
    if ship.arms_big:
        end_time=ship.arms_gig_starttime+10
        if time.time()>end_time:
            ship.arms_big=False
        setting.bullet_width *= 20
    if len(bullets) < setting.bullet_maxcount:
        new_bullet = Bullet(screen, setting, ship)
        bullets.add(new_bullet)



def create_alien(setting,screen,aliens,stats):
    setting.alien_count += int(stats.score/15)
    setting.alien_speed += int(stats.score/20)/5
    if len(aliens)==0:
        for i in range(setting.alien_count):
            new_alien=Alien(screen,setting)
            aliens.add(new_alien)

def check_events_KeyDown(ship,event,setting,screen,bullets,stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ship,setting,screen,bullets,stats)
    elif event.key==pygame.K_z:
        ship.arms_big=True
        ship.arms_gig_starttime=time.time()



def check_events_KeyUp(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def play_start(stats,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)
        stats.settings.copy_life=stats.settings.ship_limit
        stats.game_start=True

def check_events(ship,setting,screen,bullets,stats,play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_events_KeyDown(ship,event,setting,screen,bullets,stats)
        elif event.type==pygame.KEYUP:
            check_events_KeyUp(ship,event)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_start(stats, play_button, mouse_x, mouse_y)

def update_screen(setting,screen,ship,bullets,aliens,button,stats,score):
    screen.fill(setting.bg_color)
    ship.blitme()
    aliens.draw(screen)
    ship.update()
    score.draw_score()
    if stats.game_start is False:
        button.draw_button()
    for bullent in bullets.sprites():
        bullent.draw_bullet()
        bullent.update()
    pygame.display.flip()

def update_bullet(bullets,setting,aliens,stats):
    for bullent in bullets.copy():
        if bullent.rect.bottom < 0 or bullent.rect.left<0 or bullent.rect.right>setting.width:
            bullets.remove(bullent)
    collsisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collsisions:
        stats.score += 1

def update_aliens(aliens,setting,ship,stats,bullents,screen):
    for alien in aliens.sprites():
        alien.update()
        if alien.rect.bottom>setting.heigh:
            aliens.remove(alien)
    if pygame.sprite.spritecollideany(ship,aliens):
        if stats.settings.copy_life>0:
            stats.settings.copy_life -= 1
            aliens.empty()
            bullents.empty()
            create_alien(setting,screen,aliens,stats)
            ship.center_ship()
            time.sleep(0.5)
        else:
            if stats.score>stats.max_score:
                stats.max_score=stats.score
                try:
                    dir={'maxscore':stats.max_score}
                    with open('max_score.json','w') as fileobject:
                        json.dump(dir,fileobject)
                except:
                    pass
            stats.score = 0
            stats.game_start=False
            pygame.mouse.set_visible(True)
