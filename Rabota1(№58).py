"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№58).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17.12.2020
Дата последней модификации: 17.12.2020
Описание: Решение задачи №58 Практикума №1
Описание: Задана строка символов, в которой встречается символ «.». Поставить после каждого такого символа системное время ПК.
# Версия Python: 3.9
"""

from datetime import datetime
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

now = str(datetime.now())

for string in list_strings:
    print(string.replace('.', '.' + now))
