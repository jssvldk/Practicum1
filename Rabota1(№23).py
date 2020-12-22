"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№23).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 16.12.2020
Дата последней модификации: 16.12.2020
Описание: Решение задачи №23 Практикума №1
Описание: Даны двещественные числа X и Y. Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y) в противном случае.
# Версия Python: 3.9
"""

import math
x = float(input("Введите вещественное число x:"))
y = float(input("Введите вещественное число y:"))
if x > y:
    z = math.sqrt(x * y)
    print(z)
else:
    z = math.log(x + y, math.e)
    print(z)
