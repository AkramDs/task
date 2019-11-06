class Car:
    def __init__(self, make, model, year, distance, fuel = 70, odometer = 0):
        self.make = make
        self.model = model
        self.year = year
        self.distance = distance
        self.fuel = fuel
        self.odometer = odometer

        print(f'{model} от {make} {year}г. Произвотства \n')

    def drive(self, distance, fuel):
        self._add_distance()
        self._subtract_fuel()

        #print('Поройденый путь', self.distance / fuel)
        print('Потрачено топлива:',self.fuel, 'на:', self.fuel * 10, 'от:', self.distance)

        if fuel / distance < 0.1 or fuel == 0:
            print('Need more fuel, please, fill more!')

        else:
            print('Let\'s drive')

    def _add_distance(self):
        self.odometer += distance
    
    def _subtract_fuel(self):
        self.fuel / distance * 100


make = input('Введите марку: ')
model = input('Введите модель: ')
year = int(input('Введите год: '))
distance = int(input('Введите растояние: '))
fuel = int(input('Введите количество топлива: '))

# make = 'makers'
# model = 'python'
# year = 2019
# distance = 200
# fuel = 19

some_car = Car(make, model, year, distance, fuel)
some_car.drive(distance, fuel)
