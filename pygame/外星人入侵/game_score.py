import pygame.font

class GameScore:
    def __init__(self,screen,setting,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats
        self.setting=setting

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score(self.stats.score,stats.max_score,self.setting.copy_life)

    def prep_score(self,score,max_score,life):
        score_str=str(score)
        max_score_str=str(max_score)
        life=str(life)
        self.score_image = self.font.render('Life value: '+life+"   Current score:"+score_str+"  Best in history:"+max_score_str, True, self.text_color, self.setting.bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.setting.width-20
        self.score_rect.top=self.screen_rect.top+20

    def draw_score(self):
        self.screen.blit(self.score_image,self.score_rect)
