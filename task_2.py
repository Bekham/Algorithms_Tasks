"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


# Вывод: Добавлена проверка и вывод ошибки при неверном добавлении значения в левую  и правую ветки, а также
# при задании нового значения в существующей ветке.

class ChildTest(Exception):
    def __init__(self, root, left_child, right_child):
        self.root = root
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        if self.left_child:
            if self.left_child > self.root:
                return f'You select a wrong side of tree! ' \
                       f'Left_child ({self.left_child}) must be smaller Root tree ({self.root}) !'
        if self.right_child:
            if self.right_child < self.root:
                return f'You select a wrong side of tree! ' \
                       f'Right_child ({self.right_child}) must be bigger Root tree ({self.root})!'


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            if self.root < new_node:
                raise ChildTest(self.root, new_node, None)
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if self.left_child.get_root_val() < new_node:
                raise ChildTest(self.left_child.get_root_val(), new_node, None)
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            if self.root > new_node:
                raise ChildTest(self.root, None, new_node)
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if self.right_child.get_root_val() > new_node:
                raise ChildTest(self.right_child.get_root_val(), None, new_node)
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if self.right_child:
            if BinaryTree.get_right_child(self).get_root_val() > obj:
                raise ChildTest(BinaryTree.get_right_child(self).get_root_val(), None, obj)
            self.root = obj
        if self.left_child:
            if BinaryTree.get_left_child(self).get_root_val() < obj:
                raise ChildTest(BinaryTree.get_left_child(self).get_root_val(), obj, None)
            self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(f'Root tree: {r.get_root_val()}')
r.insert_left(6)
r.insert_left(5)
print(f'Left child first: {r.get_left_child().get_root_val()}')
# r.insert_left(7)  # Вывод ошибки при добавлении в левую ветку значения больше, чем предыдущее
r.insert_right(12)
print(f'Right child first: {r.get_right_child().get_root_val()}')
r.insert_right(14)
print(f'Right child second: {r.get_right_child().get_root_val()}')
# r.insert_right(11)  # Вывод ошибки при добавлении в правую ветку значения больше, чем предыдущее
# r.get_right_child().set_root_val(10)  # Вывод ошибки при замене в правой ветке корневого значения на неверное
# print(r.get_right_child().get_root_val())
