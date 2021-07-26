"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
# Вывод: по всем функциям двусторонняя очередь выполняется быстрее. Наибольшее различие по времени выполнения
# наблюдается при удалении элементов из начала списка/очереди(особенно ярко выражено при увеличении длинны списка)"""

from collections import deque
from timeit import timeit


def list_insert(n):
    lst = []
    for i in range(n):
        lst.insert(i, i)
    return lst


def deque_left(n):
    dlst = deque()
    for i in range(n):
        dlst.appendleft(i)
    return dlst


def list_pop(n):
    lst = list_insert(n)
    for i in range(len(lst)):
        x = lst.pop(0)


def deque_popleft(n):
    dlst = deque_left(n)
    for i in range(len(dlst)):
        x = dlst.popleft()


def list_extend(n):
    lst_1 = deque_left(n)
    lst_2 = deque_left(n)
    lst_2.extend(lst_1)
    return lst_1


def deque_extendleft(n):
    dlst_1 = deque_left(n)
    dlst_2 = deque_left(n)
    dlst_1.extendleft(dlst_2)
    return dlst_1


print('Создание списка: ', timeit("list_insert(10000)", "from __main__ import list_insert", number=100))
print('Создание очереди: ', timeit("deque_left(10000)", "from __main__ import deque_left", number=100))
print('Удаление элементов из начала списка: ',
      timeit("list_pop(10000)", "from __main__ import list_pop", number=100))
print('Удаление элементов из начала очереди: ',
      timeit("deque_popleft(10000)", "from __main__ import deque_popleft", number=100))
print('Объединение двух списков: ',
      timeit("list_extend(10000)", "from __main__ import list_extend", number=100))
print('Объединение двух очередей: ',
      timeit("deque_extendleft(10000)", "from __main__ import deque_extendleft", number=100))
