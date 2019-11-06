text = input().lower()
iteration = int(input())
# print(ord('a')) Буквы в цифры
# print(chr(97), chr(122)) Цифры в буквы

def crypting(text, iteration):
    crypting = ''

    for i in text:
        if i == ' ':
            crypting += ' '
            continue
        
        number = ord(i)
        number += iteration

        if number < 97:
            number += 26
        elif number > 122:
            number -= 26

        crypting += chr(number)
    return crypting

total = crypting(text, -iteration)

print(total.upper())
