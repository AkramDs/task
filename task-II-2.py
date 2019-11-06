while True:
    try:
        a = int(input('Ведите первое число: '))
        b = int(input('Ведите второе число: '))

        print('Итог: ', a / b)
        print('Остаток: ', a % b)
        try:
            d = input('Хотите ли вы продолжить "Д" или нет "Н" ').lower()
        except:
            print('Водите только "Д" или "Н"')
            break

        if d == 'н':
            break
        else:
            continue

    except ValueError:
        print('Водите только чилсла')
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
