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
# В данном примере была предпринята попытка применить recordclass для оптимизации затрат оперативной памяти, однако
# резульаты рассчета используемой памяти остались практически идентичны, как и время рассчета. Вероятно данный метод
# хорошо проявляет себя при работе с большими массивами данных.
import memory_profiler
from random import randrange
from recordclass import recordclass
from timeit import timeit


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        # del m1,m2
        return mem_diff

    return wrapper


@decor
def get_jokes(count, key):
    """Generating a given number of jokes"""
    jokes = []
    text = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    text.append(nouns)
    text.append(adverbs)
    text.append(adjectives)
    while count:
        num_word = []
        joke = ''
        for i in range(0, len(text)):
            num_word.append(randrange(len(text[i])))
            joke += text[i][num_word[i]] + ' '
            if key:
                text[i].remove(text[i][num_word[i]])
        jokes.append(joke)
        count -= 1
    print(jokes)


@decor
def get_jokes_mod(count, key):
    """Generating a given number of jokes"""
    jokes = set()
    text_jokes = recordclass('text_jokes', ('nouns', 'adverbs', 'adjectives'))
    text = text_jokes(nouns=["автомобиль", "лес", "огонь", "город", "дом"],
                      adverbs=["автомобиль", "лес", "огонь", "город", "дом"],
                      adjectives=["веселый", "яркий", "зеленый", "утопичный", "мягкий"])
    for j in range(count):
        joke = str()
        for i in range(3):
            word_i = randrange(len(text[i]))
            joke += text[i][word_i] + ' '
            if key:
                text[i].remove(text[i][word_i])
        jokes.add(joke)
    print(jokes)


if __name__ == '__main__':
    no_repeat = True  # флаг, разрешающий или запрещающий повторы слов в шутках (True - запрет, Fasle - разрешение
    # повторов)
    print(f'Количество памяти, затраченное на выполение оригинального задания: {get_jokes(4, no_repeat)}')
    print(f'Количество памяти, затраченное на выполение модифицированного задания: {get_jokes_mod(4, no_repeat)}')
    print('Время работы оригинального скрита: ',
          timeit('get_jokes(4, True)',
               'from __main__ import get_jokes',
               number=1))
    print('Время работы модифицированного скрита: ',
          timeit(
              'get_jokes_mod(4, True)',
              'from __main__ import get_jokes_mod',
              number=1))
