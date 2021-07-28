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
# при использовании __slots__ и указании сохранять атрибуты класса в кортеже существенно уменьшился объем оперативной
# памяти, занимаемый классом, как и время его
# опроса.
from pympler import asizeof
from timeit import timeit

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])

    def __str__(self):
        enter = ''
        for row in self.matrix:
            enter += f'{" ".join(map(str, row))}\n'
        return enter


m1 = Matrix([[10, 2, 3], [3, 4, 3], [9, 4, 67]])
m2 = Matrix([[3, 76, 23], [4, 34, 45], [76, 43, 21]])
# print(f'{m1}+\n{m2}=')
# print(m1 + m2)
print('Размер первой оригинальной матрицы: ', asizeof.asizeof((m1)))
print('Размер второй оригинальной матрицы: ', asizeof.asizeof((m2)))


class Matrix_mod:
    __slots__ = ("matrix")
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ])

    def __str__(self):
        enter = ''
        for row in self.matrix:
            enter += f'{" ".join(map(str, row))}\n'
        return enter


m1_mod = Matrix_mod([[10, 2, 3], [3, 4, 3], [9, 4, 67]])
m2_mod = Matrix_mod([[3, 76, 23], [4, 34, 45], [76, 43, 21]])
# print(f'{m1_mod}+\n{m2_mod}=')
# print(m1_mod + m2_mod)
print('Размер первой модифицированной матрицы: ', asizeof.asizeof((m1_mod)))
print('Размер второй модифицированной матрицы: ', asizeof.asizeof((m2_mod)))
m = m1 + m2
m_mod = m1_mod + m2_mod
print('Время работы оригинального скрита: ',
        timeit(
            'm',
            'from __main__ import m',
            number=1))
print('Время работы модифицированного скрита: ',
    timeit(
        'm_mod',
        'from __main__ import m_mod',
        number=1))