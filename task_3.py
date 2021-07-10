"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.

Итог выполнения задания: Первый вариант выполнится быстрее по причине того что, для него соответствует двадратичная
функиця, а для второго варианта - кубическая.
"""


def top_company_1(company_list):  # Итог O(N**2)
    all_money = []  # O(1)
    top_company = ['', '', '']  # O(1)
    for k in company_list.values():  # O(N)
        all_money.append(k)  # O(1)
    all_money.sort(reverse=True)  # O(NLogN)
    for i, j in company_list.items():  # O(N)
        if j in all_money[:3]:  # O(N)
            top_company[all_money.index(j)] = i  # O(1)
    for top in range(0, 3):  # O(N)
        print(f'{top + 1}. {top_company[top]}:  {all_money[top]} млн. долларов')


def top_company_2(company_list):  # Итог O(N**3)
    money_sorted_values = sorted(company_list.values(), reverse=True)  # O(NLogN)
    sorted_top = {}  # O(1)
    count = 0  # O(1)
    for i in money_sorted_values:  # O(N)
        for k in company_list.keys():  # O(N)
            if company_list[k] == i:  # O(1)
                sorted_top[k] = company_list[k]  # O(1)
                count += 1  # O(1)
                for m, j in sorted_top.items():  # O(N)
                    if count == 3:  # O(1)
                        print(f'{m}: {j}  млн. долларов')
                # break


company_info = {'Alibaba Group Holding': 21450,
                'Berkshire Hathaway': 81417,
                'Alphabet': 34343,
                'China Construction Bank': 38610,
                'Microsoft': 39240,
                'Bank of America Corp.': 27430,
                'JPMorgan Chase & Co.': 36431,
                'Industrial & Commercial Bank of China': 45195,
                'Agricultural Bank of China': 30701,
                'Ping An Insurance': 21627,
                'Bank of China': 27127,
                'Saudi Aramco': 88211,
                'Apple': 55256
                }
print('Варинат 1:')
top_company_1(company_info)
print('Варинат 2:')
top_company_2(company_info)
