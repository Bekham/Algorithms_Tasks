"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(round(time.perf_counter() - start_time, 5), 'sec')
        return res

    return wrapped


@time_of_function  # Создание словаря
def dict_append(massive):
    dict_add = {}
    for l in range(len(massive)):  # O(n)
        dict_add[l] = l  # O(1)
    return dict_add


@time_of_function  # Изменение словаря
def dict_update(new_dict):
    for k, j in new_dict.items():  # O(n)
        new_dict[k] = j * (len(new_dict) - j) * (1 / 2)  # O(1)
    return new_dict  # O(1)


@time_of_function  # Удаление словаря
def dict_del(new_dict):
    new_dict.clear()  # O(1)
    return new_dict  # O(1)


@time_of_function  # Создание списка
def list_append(massive):
    list_add = []
    for m in range(len(massive)):  # O(n)
        list_add.append(m)  # O(1)
    return list_add  # O(1)


@time_of_function  # Изменение списка
def list_update(new_list):
    for k in range(len(new_list)):  # O(n)
        new_list[k] = k * (len(new_list) - k) * (1 / 2)  # O(1)
    return new_list  # O(1)


@time_of_function  # Удаление списка
def list_del(new_list):
    new_list.clear()  # O(1)
    return new_list  # O(1)


mass_test = []
for i in range(1000000):
    mass_test.append(i)
print('Заполнение словаря:', end=' ')
new_d = dict_append(mass_test)
print('Изменение словаря:', end=' ')
dict_update(new_d)
print('Удаление словаря:', end=' ')
dict_del(new_d)
print('-' * 35)
print('Заполнение списка:', end=' ')
new_l = list_append(mass_test)
print('Изменение списка:', end=' ')
list_update(new_l)
print('Удаление списка:', end=' ')
list_del(new_l)

# Итог: Сложность выполнения индентичных опреаций при работе со словарем и списком одинакова.
# Однако, скорость выполнения операций при работе со списком выше.
