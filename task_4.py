"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
# OrderedDict работает медленнее обычного словаря, однако возможность сохранять свой порядок при добавлении ключей
# дают ему преимущество при определенных ситуациях при написании более лаконичного кода и удобства использования"""

from collections import OrderedDict
from timeit import timeit


def dict_range(n):
    dct = {}
    for i in range(n):
        dct[i] = i
    return dct


def ordered_range(n):
    odct = OrderedDict()
    for i in range(n):
        odct[i] = i
    return odct


def dict_move(n):
    dct = dict_range(n)
    for i in range(n - 1):
        x = dct.pop(i)
        dct[i] = x
    return dct


def ordered_move(n):
    odct = ordered_range(n)
    for i in range(n - 1):
        odct.move_to_end(i, last=True)
    return odct


def dict_popitem(n):
    dct = dict_range(n)
    for i in range(n):
        x = dct.popitem()
    return dct


def ordered_popitem(n):
    odct = ordered_range(n)
    for i in range(n):
        x = odct.popitem(last=True)
    return odct


print('Создание словаря: ',
      timeit("dict_range(10000)", "from __main__ import dict_range", number=100))
print('Создание упорядоченного словаря: ',
      timeit("ordered_range(10000)", "from __main__ import ordered_range", number=100))
print('Перемещение элементов словаря из начала в конец: ',
      timeit("dict_move(10000)", "from __main__ import dict_move", number=100))
print('Перемещение элементов упорядоченного словаря из начала в конец: ',
      timeit("ordered_move(10000)", "from __main__ import ordered_move", number=100))
print('Удаление элементов словаря: ',
      timeit("dict_popitem(10000)", "from __main__ import dict_popitem", number=100))
print('Удаление элементов упорядоченного словаря: ',
      timeit("ordered_popitem(10000)", "from __main__ import ordered_popitem", number=100))
