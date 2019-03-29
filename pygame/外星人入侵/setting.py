class Settings():
    """
    用来保存游戏相关设置
    """
    def __init__(self):
        self.width=1200
        self.heigh=800
        self.size=(self.width,self.heigh)
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1
        self.bullet_color=(60,60,60)
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_heigh=15
        self.bullet_size=(self.bullet_width,self.bullet_heigh)
        self.bullet_maxcount=3
        self.alien_speed=1
        self.alien_count=5