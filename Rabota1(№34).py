"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№34).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 16.12.2020
Дата последней модификации: 16.12.2020
Описание: Решение задачи №34 Практикума №1
Описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами первую и вторую половины массива.
# Версия Python: 3.9
"""

import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)
for i in range(len(a) // 2):
    a[i], a[i + len(a) // 2] = a[i + len(a) // 2], a[i]
    
print(a)
