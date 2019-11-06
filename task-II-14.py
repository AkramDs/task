mass = float(input('Введите массу: '))
weight = float(input('Введите количество лет: '))

for i in range(int(weight)):
    print('Ваш вес:', mass * 0.165)
    mass += 1
