"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
"""Пример создания стека через ООП"""


class StackClass:

    def __init__(self):
        self.elems = []
        self.max_el = 3
        self.all_el = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) < self.max_el:
            self.elems.append(el)
            if len(self.elems) > 1:
                self.all_el.pop()
                self.all_el.append(self.elems)
            else:
                self.all_el.append(self.elems)
        else:
            self.elems = []
            self.elems.append(el)
            self.all_el.append(self.elems)

    def get_all(self):
        return self.all_el

    def max_val(self):
        return self.max_el

    def pop_out(self):
        if len(self.elems) > 0:
            return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(55.5)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(9)
    SC_OBJ.push_in(10)
    print(SC_OBJ.stack_size())
    print(SC_OBJ.get_all())
    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 10

    # узнаем размер текущего стека
    print(SC_OBJ.stack_size())  # -> 2

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)
    print(SC_OBJ.get_all())
    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 10

    # вновь узнаем размер текущего стека
    print(SC_OBJ.stack_size())  # -> 1

    # узнаем максимальное количество в стеке
    print(SC_OBJ.max_val())

    # итоговый набор стеков
    print(SC_OBJ.get_all())
