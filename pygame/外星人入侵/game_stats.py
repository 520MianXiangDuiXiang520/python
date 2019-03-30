import json

class GameStats():
    def __init__(self,setting):
        self.settings=setting
        self.reset_stats()
        self.game_start=False
        self.score=0
        try:
            with open('max_score.json') as fileobject:
                s=json.load(fileobject)
                self.max_score=s['maxscore']
        except:
            self.max_score=0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit