"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict


def d_dict():
    d_16 = defaultdict(list)
    a = input('Введите первое число: ')
    d_16[a] = list(a)
    b = input('Введите второе число: ')
    d_16[b] = list(b)
    sum_num = int(''.join(d_16[a]), 16) + int(''.join(d_16[b]), 16)
    mul_num = int(''.join(d_16[a]), 16) * int(''.join(d_16[b]), 16)
    print(f'Сумма чисел {d_16[a]} и {d_16[b]}: {list(hex(sum_num))[2:]}')
    print(f'Произведение чисел {d_16[a]} и {d_16[b]}: {list(hex(mul_num))[2:]}')


class HexNumber:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def __add__(self, other):
        return list(hex(int(''.join(self.num_a), 16) + int(''.join(self.num_b), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_a), 16) * int(''.join(self.num_b), 16)))[2:]


def class_hex():
    a = list(input('Введите первое число: '))
    b = list(input('Введите второе число: '))
    sum_num = HexNumber(a, b) + HexNumber(a, b)
    mul_num = HexNumber(a, b) * HexNumber(a, b)
    print(f'Сумма чисел {a} и {b}: {sum_num}')
    print(f'Произведение чисел {a} и {b}: {mul_num}')


d_dict()
class_hex()
