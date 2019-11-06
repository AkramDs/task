numbers = list(map(int, input()))
iteration = int(input())

print(numbers)

def crypting(numbers, iteration=3):
    crypting = ''

    for i in range(numbers.__len__()):
        crypting += str(numbers[i - iteration])

    return crypting

total = crypting(numbers, iteration)

print(total)
