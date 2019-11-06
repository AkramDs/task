a = input('Ведите строку: ')

symbol_up = 0
symbol_down = 0

for i in range(a.__len__()):
    test = a[i]
    if test == ' ':
        continue
    elif test.isupper():
        symbol_up = symbol_up + 1
    else: 
        symbol_down = symbol_down + 1

if symbol_up % symbol_down == 0:
    print(50.0)
else:
    print('Загланые относително строчных: ', (symbol_up / symbol_down) * 100)
    print('Cтрочных относително загланые: ', (symbol_down / symbol_up) * 100)

