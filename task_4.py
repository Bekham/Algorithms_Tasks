"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib as h
from uuid import uuid4
import random as r


def memorize(func):
    def g(url, memory={}):
        find_url = memory.get(url)
        if find_url is None:
            find_url = func(url)
            memory[url] = find_url
        print(memory)
        return find_url

    return g


@memorize
def url_hash(_url_):
    salt = uuid4().hex
    find_url = [h.sha256(_url_.encode('utf-8') + salt.encode('utf-8')).hexdigest(), salt]
    return find_url


for i in range(10):
    url_new = 'www.'
    for j in range(1, r.randint(3, 8)):
        url_new += chr(r.randint(97, 122))
    url_new += '.com'
    url_hash(url_new)
