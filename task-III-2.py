string = 'сон машина стол книга девочка' + ' ' #'abc cbccwa asbc' + ' ' # input('Enter string: ') + ' '
counter = ''
total_list = []

def havelist(string):
    total_list.append(string)

for i in range(string.__len__()):
    if string[i] != ' ':
         counter += string[i]
    else:
        havelist(counter)
        counter = ''
        continue
del counter

#print(sorted(total_list, key=len))

total = ''
total_list1 = sorted(total_list, key=len)
for i in range(total_list1.__len__()):
    total += str(total_list1.pop()) + ' '

print(total)
