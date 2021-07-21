"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
# Вывод: для таких небольших задач cProfile не годится - слишком малое время обработки. Необходимо число примерно n^100
# для отображения минимально возможного времени расчета.
# Из пяти реализаций эффективнее всего работает функция 3 и 4, возможно, за счет исключения математического решения из
# кода и использования возможностей среза - базовой функции.
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return str(enter_num)[::-1]


def revers_5(enter_num):
    return int("".join(reversed(str(enter_num))))


print(timeit("revers_1(1234567891011121314151617181920)", "from __main__ import revers_1", number=10000))
print(timeit("revers_2(1234567891011121314151617181920)", "from __main__ import revers_2", number=10000))
print(timeit("revers_3(1234567891011121314151617181920)", "from __main__ import revers_3", number=10000))
print(timeit("revers_4(1234567891011121314151617181920)", "from __main__ import revers_4", number=10000))
print(timeit("revers_5(1234567891011121314151617181920)", "from __main__ import revers_5", number=10000))
run('revers_1(1234567891011121314151617181920)')
run('revers_2(1234567891011121314151617181920)')
run('revers_3(1234567891011121314151617181920)')
run('revers_4(1234567891011121314151617181920)')
run('revers_5(1234567891011121314151617181920)')
