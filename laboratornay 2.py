#Дружинина Дарья R3142 412936
import csv
from random import randint
#Задание№1
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    flag = 0
    for row in table:
        if len(list(row)[1]) > 30:
            flag += 1
    print(flag)

#Задание№2
flag = []
author = input('Введите автора :\n')
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    book = csv.reader(csvfile, delimiter=';')
    for row in book:
        if (list(row)[4] == author or list(row)[3] == author) and (float(list(row)[7]) >= 150):
                flag.append(list(row)[1])
    print('Книги автора, цена которых 150 рублей и выше:\n')
    for books in flag:
        print(books)

#Задание№3
result = [randint(1, 9410) for x in range(20)]
flag = []
with open('books.csv', encoding='windows-1251') as csvfile:
    book = [i for i in csv.reader(csvfile, delimiter = ';')]
    for i in result:
        reader_list = list(book)
    for i in flag:
        row = reader_list[i]
    with open('resultat.txt', 'w') as f:
        for i in range(1,21):
            f.writelines(f'{str(i)} {book[i][3]}.  {book[i][1]} -  {book[i][6]} \n')

#Доп задания
tag = []
inf = []
with open('books-en.csv', 'r') as csvfile:
    line = csvfile.readline()
    for row in csvfile:
        book = row.split(';')
        tag.append(book[4])
        name = str(book[1])
        downloads = int(book[-2])
        inf += [[name, downloads]]
    inf.sort(key = lambda k:k[1], reverse = True)
    print('Теги:', set(tag))
    print('20 самых популярных книг:')
    for i in range(20):
        print(f'{i + 1}. {inf[i][0]}')

