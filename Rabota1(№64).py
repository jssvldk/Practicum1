"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№64).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 18.12.2020
Дата последней модификации: 18.12.2020
Описание: Решение задачи №64 Практикума №1
Описание: Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
# Версия Python: 3.9
"""

import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)
