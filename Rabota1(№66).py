"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№66).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 18.12.2020
Дата последней модификации: 18.12.2020
Описание: Решение задачи №66 Практикума №1
Описание: Для вводимых чисел определить процент положительных и отрицательных чисел. При вводе числа −65432 закончить работу.
# Версия Python: 3.9
"""

import re

list_numbers = []

count_positive = 0
count_negative = 0

while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)

    if number * -1 == 65432:
        break

    list_numbers.append(number)

    if number < 0:
        count_negative += 1
    else:
        count_positive += 1


one_percent = 100 / len(list_numbers)
print("Процент положительных чисел:", one_percent * count_positive)
print("Процент отрицательных чисел:", one_percent * count_negative)
