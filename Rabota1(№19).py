Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№19).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №19 Практикума №1
Описание: Даны вещественные числа: X, Y, Z. Определить, существует ли треугольник с такими длинами сторон и, если существует, будет ли он прямоугольным.
# Версия Python: 3.9
"""

X = int(input("Сторона 1:"))
Y = int(input("Сторона 2:"))
Z = int(input("Сторона 3:"))
if (X+Y <=Z) or (Y+Z <=X) or (Z+X <= Y):
    print("Треугольник с такими сторонами не существует:")
if (X > Y and X > Z) and (X**2 == Y**2 + Z**2):
    print("Треугольник прямоугольный:")
elif (Y > X and Y > Z) and (Y ** 2 == X ** 2 + Z ** 2):
    print("Труегольник прямоугольный")
elif (Z > Y and Z > X) and (Z ** 2 == Y ** 2 + X ** 2):
    print("Труегольник прямоугольный:")
else:
    print("Труегольник не прямоугольный:")