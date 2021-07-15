"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


word = input('Enter the word: ')
unique_list = set()
for front in range(len(word)):
    if front > 0:
        unique_list.add(hash(word[front:]))
    for end in range(len(word)):
        if front != end and front < end:
            unique_list.add(hash(word[front:end]))
print(len(unique_list))
