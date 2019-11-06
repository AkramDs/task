print(
'''0) google_kazakstan.txt
1) google_paris.txt
2) google_uar.txt
3) google_kyrgystan.txt
4) google_san_francisco.txt
5) google_germany.txt
6) google_moscow.txt
7) google_sweden.txt''')

a = input('\nВ какой файл вы хотите записать текст: ')
b = input('Что вы хотите записать: ')

c = ['google_kazakstan.txt', 'google_paris.txt', 'google_uar.txt',
'google_kyrgystan.txt', 'google_san_francisco.txt', 'google_germany.txt',
'google_moscow.txt', 'google_sweden.txt']

def write(file):
    file = open(file, 'w')
    file.write(b)
    file.close()

for x in c:
    for i in range(c.__len__()):
        try:
            if x == a:
                write(x)
            elif int(a) == c.index(x):
                write(x)

        except ValueError:
            print('ValueError')
            break
