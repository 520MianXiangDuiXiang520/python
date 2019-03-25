class Gun:
    type=''
    bullet_count=0
    def __init__(self,type,bullet_count):
        self.type=type
        self.bullet_count=bullet_count

class Soldier:
    name=''
    gun=''
    def __init__(self,name,gun):
        self.name=name
        self.gun=gun
    def add_bullet(self,add_count):
        self.gun.bullet_count+=add_count
        print("%s  补充 %d 颗子弹后剩余子弹数 %d " % (self.name,add_count,self.gun.bullet_count))
    def shoot(self,less_count):
        self.gun.bullet_count-=less_count
        print("%s 用 %s 射击 %d 次后剩余子弹数 %d " % (self.name, self.gun.type, less_count, self.gun.bullet_count))

ak47=Gun('ak47',500)
fugui=Soldier('fugui',ak47)
fugui.shoot(100)
fugui.add_bullet(300)