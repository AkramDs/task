from functools import partial

class airbus:
    def __init__(self, make, model, year, max_speed, fly_range, odometer = 0, is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def turn_off(self):
        #a = partial(bool, is_flying = True)
        self.is_flying = True
    
    def land(self):
        #a = partial(bool, is_flying = False)
        self.is_flying = False

    def fly(self):
        self.odometer += fly_range

make = input('Введите марку: ')
model = input('Введите модель: ')
year = int(input('Введите год проезлодства: '))
max_speed = int(input('Введите максимальную скорость: '))
fly_range = int(input('Введите растояние полёта: '))

# make = 'Banana'
# model = 'Cargabob'
# year = 2013
# max_speed = 120
# fly_range = 200

airplane = airbus(make, model, year, max_speed, fly_range)

airplane.turn_off()
print(airplane.is_flying)
airplane.fly()
print('odometer =', airplane.odometer)
airplane.land()
print(airplane.is_flying)
