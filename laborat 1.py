#Дружинина Дарья R3142 412936
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[40m'

#Задание№1
print('Флаг Тайланда')
for i in range(10):
    if i == 0 or i == 5:
        print(f'{RED}{"  " * 10} {END}')
    if i == 1 or i == 4:
        print(f'{WHITE}{"  " * 10} {END}')
    if i == 2 or i == 3:
        print(f'{BLUE}{"  " * 10} {END}')

#Задание№2
print('\n')
print('Узор f')
print('Введите длину узора')
n = int(input())
print('Введите ширину узора')
b = int(input())
for i in range(b):
    print(f'{WHITE}{"  " * 2}{END}', f'{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 3}{END}'*n, sep='')
    print(f'{WHITE}{"  " * 2}{END}', f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 2}{END}'*n, sep='')
    print(f'{BLACK}{"  " * 2}{END}', f'{WHITE}{"  " * 3}{BLACK}{"  " * 2}{END}'*n, sep='')

#Задание№3
print('График у = 1/х')
result = [[0 for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if j == 0 and i <= 4:
            result[i][j] = "!"
        if (j == 1 and i == 5) or (j == 2 and i == 6) or (j == 3 and i == 7) or (j == 4 and i == 8):
            result[i][j] = "!"
        if j >=5 and i==9:
            result[i][j] = "!"
for i in range(10):
    for j in range(10):
        print(result[i][j], end='')
    print()

#Задание№4
file = open('sequence.txt')
list = []
for i in file:
    if float(i) > 0:
     list.append(float(i))
file.close()
bol5=0
men5=0
for i in list:
        if i > 5:
            bol5+=1
        if i > 0 and i < 5:
            men5+=1
print('>5:')
print(f'{BLACK}{" " * int(bol5/(bol5+men5)*100)}{END}', '\n')
print('<5:')
print(f'{BLACK}{" " * int(men5/(bol5+men5)*100)}{END}', '\n')

