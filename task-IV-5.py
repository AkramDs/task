class Guns:
    def __init__(self, bullets = 30, clips = 3):
        self.bullets = bullets
        self.clips = clips

class Soldier(Guns):
    def shootting(self):
        if self.bullets >= 1 or self.clips >= 1:
            print('shot')
        else:
            print('Not bullets')

class Act_of_Shooting(Soldier):
    pass

man = Act_of_Shooting()
man.shootting()
