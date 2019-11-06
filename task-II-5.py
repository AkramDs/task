print(
'''
Ведите кольчество людей в класах
''')

class_room1 = int(input('Первый класс: '))
class_room2 = int(input('Второй класс: '))
class_room3 = int(input('Третий класс: '))

print('\n')

try:
    if class_room1 % 2 == 0:
        print(int(class_room1 / 2))
    else:
        print(int((class_room1 / 2) + (class_room1 % 2)))

    if class_room2 % 2 == 0:
        print(int(class_room2 / 2))
    else:
        print(int((class_room2 / 2) + (class_room2 % 2)))

    if c % 2 == 0:
        print(int(class_room3 / 2))
    else:
        print(int((class_room3 / 2) + (class_room3 % 2)))
except ZeroDivisionError:
    print('На ноль делить нельзя!')
