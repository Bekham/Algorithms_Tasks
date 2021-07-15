"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib as h
from uuid import uuid4


def pass_hash(password, s):
    hash_pass = h.sha256(password.encode('utf-8') + s.encode('utf-8')).hexdigest()
    print(hash_pass)
    return hash_pass


print('User: Admin')
salt = uuid4().hex
hash_pass_first = pass_hash(input('Enter your password: '), salt)

with open('less_3_task_2.txt', 'w', encoding='utf-8') as f:
    f.write(f'Admin : {hash_pass_first} : {salt} : ' + '\n')
pass_second = input('Enter your password again: ')
with open('less_3_task_2.txt', 'r', encoding='utf-8') as f:
    correct = False
    for line in f:
        if line.split(' : ')[0] == 'Admin' and pass_hash(pass_second, line.split(' : ')[2]) == line.split(' : ')[1]:
            correct = True
    if correct:
        print('Correct!!!')
    else:
        print('Wrong pass!!!')
