import random

class Hero:
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level
    
    def upLevel(self, changeLevel):
        self.level += changeLevel

class Soldier:
    def __init__(self, number):
        self.number = number

    def goToHero(self, hero):
        return f'{self.number} иду за {hero.name}'

class Play:
    lostLevel = 0

    def teamCreater(self, teamRange):
        self.teamRed = []
        self.teamBlue = []

        for i in range(teamRange):
            number = random.randint(0, 1)
            #print(number)

            if number == 1:
                soldierRed = Soldier(i)
                self.teamRed.append(soldierRed)
            
            elif number == 0:
                soldierBlue = Soldier(i)
                self.teamBlue.append(soldierBlue)
            
            else:
                soldierRed = Soldier(i)
                self.teamRed.append(soldierRed)

                soldierBlue = Soldier(i)
                self.teamBlue.append(soldierBlue)

    
    def StartGame(self, gazgyl, linus):
        teamSoldierRed = random.randint(0, self.teamRed.__len__())
        teamSoldierBlue = random.randint(0, self.teamBlue.__len__())

        print(self.teamRed.__len__(), self.teamBlue.__len__())
        print(teamSoldierRed, teamSoldierBlue)

        goToGazgyl = self.teamRed[-teamSoldierRed].goToHero(gazgyl)
        goToLinus = self.teamBlue[-teamSoldierBlue].goToHero(linus)

        print('\n')

        if self.teamRed.__len__() > self.teamBlue.__len__():
            print(f'Победил: {gazgyl.name}')

            gazgyl.upLevel(1)

            print(goToGazgyl)
            print(f'Уровень {gazgyl.name}: {gazgyl.level}')

        elif self.teamBlue.__len__() > self.teamRed.__len__():
            print(f'Победил: {linus.name}')

            linus.upLevel(1)

            print(goToLinus)
            print(f'Уровень {linus.name}: {linus.level}')

        else:
            print('Ничия')

            self.lostLevel += 1
        
            # gazgyl.upLevel(2)
            # print(goToGazgyl)
            print(f'Уровень {gazgyl.name}: {gazgyl.level}')

            print('\n')

            #linus.upLevel(2)
            #print(goToLinus)
            print(f'Уровень {linus.name}: {linus.level}')

gazgyl_mak_uruk_traka = Hero('Газгул мак урук трака')
linus_torvalts = Hero('Линус торвалтс')

start = Play()
for _ in range(120):
    start.teamCreater(100)
    start.StartGame(gazgyl_mak_uruk_traka, linus_torvalts)

print('\n', start.lostLevel)
