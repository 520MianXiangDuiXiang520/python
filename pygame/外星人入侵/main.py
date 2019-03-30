import sys
import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_function as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from game_score import GameScore

def run_game():
    pygame.init()
    screen=pygame.display.set_mode(Settings().size)
    pygame.display.set_caption('外星人入侵')
    ship=Ship(screen,Settings())
    alien=Alien(screen,Settings())
    button=Button(Settings(), screen,'PLAY')
    stats=GameStats(Settings())
    score = GameScore(screen, Settings(), stats)
    bullets=Group()
    aliens=Group()
    gf.update_screen(Settings(), screen, ship, bullets, aliens, button,stats,score)
    while True:
        gf.check_events(ship, Settings(), screen, bullets,stats,button)
        if stats.game_start:
            gf.create_alien(Settings(), screen, aliens,stats)
            gf.update_bullet(bullets,Settings(),aliens,stats)

            gf.update_aliens(aliens,Settings(),ship,stats,bullets,screen)
            score.prep_score(stats.score,stats.max_score,stats.settings.copy_life)
            gf.update_screen(Settings(),screen,ship,bullets,aliens,button,stats,score)



if __name__ == '__main__':
    run_game()