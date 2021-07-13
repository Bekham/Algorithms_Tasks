"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random as r


def game(rand_num=0, guess_try=10):
    if guess_try == 10:
        rand_num = r.randint(0, 100)
    num = int(input('Ведите целое число от 0 до 100: '))
    guess_try -= 1
    if guess_try > 0:
        if num == rand_num:
            print(f'Вы угадали. Загаданное число {rand_num}!')
        elif num < rand_num:
            print(f'Ваше число меньше загаданного. Осталось {guess_try} попыток.')
            return game(rand_num, guess_try)
        else:
            print(f'Ваше число больше загаданного. Осталось {guess_try} попыток.')
            return game(rand_num, guess_try)
    else:
        print(f'Вы проиграли. Загаданное число: {rand_num}!')


game()
