Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№18).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №18 Практикума №1
Описание:
# Версия Python: 3.9
"""

import math
A = int(input("Ребро кубической ёмкости:"))
H = int(input("Высота цилиндрической ёмкости:"))
R = int(input("Радиус основания цилиндрической ёмкости:"))
M = int(input("Введите объем жидкости:"))
SK = A ** 3
print(SK, "Объём куба")
SC = math.pi * R ** 2 * H
print(SC, "Объём цилиндра")
if SC + SK <= M:
    print("Жидкость поместится в оба сосуда")
if SC <= M:
    print("Жидкость поместится в цилиндр")
if SK <= M:
    print("Жидкость поместится в куб")