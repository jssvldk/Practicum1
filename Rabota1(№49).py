"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№49).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17.12.2020
Дата последней модификации: 17.12.2020
Описание: Решение задачи №49 Практикума №1
Описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Определить, имеются ли в массиве два подряд идущих нуля.
# Версия Python: 3.9
"""

import random
import numpy

N = int(input("Количество элементов в массиве"))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0 and A[i-1] == 0:
        print("Два подряд нуля в ",i-1,"и",i)
