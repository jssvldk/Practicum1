Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№13).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №13 Практикума №1
Описание: Можно ли из бревна, имеющего диаметр поперечного сечения D, выпилить квадратный брус шириной A?
# Версия Python: 3.9
"""

import math
D = int(input("Введите диаметр поперечного сечения:"))
A = int(input("Введите ширину квадратного бруса:"))
A = math.sqrt(2) * A
print("Диагональ бруса равна",A)
if (A <=D):
    print("Выпилить квадратный брус шириной ",A,"возможно")
else:
    print("Выпилить квадратный брус шириной ", A, "невозможно")
