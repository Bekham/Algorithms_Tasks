"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
# Выполнение сортировки в альтернативном варианте методом слияния происходит несеолько быстрее по причине отсутствия
# рекурсии на начальном этапе деления исходного списка на элементарные списки ([x1] - в случае оригинального кода,
# [x1, x2] - в случае альтернативного кода).С увеличением длины списка разница становится более заметной.

import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def bottom_up_merge_sort(lst):
    """
    Функция деления списка, начиная с минимального количества списке [x1, x2] с сохрением отворитированных пар в
    начальном списке lst. С  увеличением k * 2 после каждого цикла for производится увеличение длины
    отсортированного списка в два раза, также с сохранением в исходном списке. За сортировку половинок списков
    отвечает отдельная функция merge(left, right)
    """
    k = 1
    while k < len(lst):
        for i in range(0, len(lst) - k, 2 * k):
            lst[i:i + 2 * k] = merge(lst[i:i + k], lst[i + k:i + 2 * k])
        k *= 2
    return lst


def merge(left, right):  # сортировка двух половинок передаваемого списка
    i, j, lst_res = 0, 0, []
    while True:
        if left[i] < right[j]:
            lst_res.append(left[i])
            i += 1
            if i == len(left):
                lst_res.extend(right[j:])
                break
        else:
            lst_res.append(right[j])
            j += 1
            if j == len(right):
                lst_res.extend(left[i:])
                break
    return lst_res


# # замеры 10
orig_list = [random.uniform(-100, 100) for _ in range(10)]
print('Оригинальный код слияния. Длина списка - 10: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(-100, 100) for _ in range(100)]

# замеры 100
print('Оригинальный код слияния. Длина списка - 100: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(-100, 100) for _ in range(1000)]

# замеры 1000
print('Оригинальный код слияния. Длина списка - 1000: ',
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(-100, 100) for _ in range(10)]

# замеры 10
print('Альтернативный код слияния. Длина списка - 10: ',
    timeit.timeit(
        "bottom_up_merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(-100, 100) for _ in range(100)]

# замеры 100
print('Альтернативный код слияния. Длина списка - 100: ',
    timeit.timeit(
        "bottom_up_merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(-100, 100) for _ in range(1000)]

# замеры 1000
print('Альтернативный код слияния. Длина списка - 1000: ',
    timeit.timeit(
        "bottom_up_merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
