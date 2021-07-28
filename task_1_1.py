"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
# Модуль Numpy позволил значитьельно сократить объем занимаемой оперативной памяти а также немного ускорить время работы
# скрипта.
import memory_profiler
import numpy as np
from timeit import timeit


def decor(func):
    def wrapper(n, **kwargs):
        m1 = memory_profiler.memory_usage()
        func(n)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff
    return wrapper


@decor
def task_one_original(n):
    list_mass = []
    for i in range(0, n):  # Создаем список из нечетных чисел, возведенных в куб
        if i % 2 != 0:
            list_mass.append(i ** 3)
    # print('Список нечетных чисел от 0 до 1000, возведенных в куб: ', list_mass)
    sum_seven_one = 0
    for i in range(len(list_mass)):  # Перебор всех элементов из созданного массива
        sum_num = 0
        for k in range(len(str(list_mass[i]))):  # Суммирование цифр в каждом отдельном элементе
            sum_num += list_mass[i] % 10 ** k // 10 ** (k - 1)
        if sum_num % 7 == 0:  # Проверка на кратность 7
            sum_seven_one += list_mass[i]
            # print(list_mass[i])
    del list_mass, sum_seven_one, sum_num


@decor
def task_one_mod(n):
    list_mass_mod = np.array([i ** 3 for i in range(n) if i % 2 != 0])
    sum_seven_one_mod = 0
    for i in range(list_mass_mod.size):  # Перебор всех элементов из созданного массива
        sum_num_mod = np.array(([int(i) for i in list(str(list_mass_mod[i]))])).sum()
        if sum_num_mod % 7 == 0:  # Проверка на кратность 7
            sum_seven_one_mod += list_mass_mod[i]

if __name__ == '__main__':
    print(f'Количество памяти, затраченное на выполение оригинального задания: {task_one_original(10001)}')
    print(f'Количество памяти, затраченное на выполение измененного задания: {task_one_mod(10001)}')
    print('Время работы оригинального скрита: ',
        timeit(
            'task_one_original(10001)',
            'from __main__ import task_one_original',
            number=1))
    print('Время работы измененного скрита: ',
        timeit(
            'task_one_mod(10001)',
            'from __main__ import task_one_mod',
            number=1))
