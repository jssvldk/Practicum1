"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№37).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 16.12.2020
Дата последней модификации: 16.12.2020
Описание: Решение задачи №37 Практикума №1
Описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Сумму элементов массива и количество положительных элементов поставить на первое и второе место.
# Версия Python: 3.9
"""

import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
A = [random.randint(-20, 20) for i in range(0, N)]

print(A)

B = 0
cym = np.sum(A)
C = np.size(A)
for i in range(N):
    if A[i] >= 0:
        B += A[i]
(A.insert(0, B))
(A.insert(1, C))

print(A)
