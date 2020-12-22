"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№44).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17.12.2020
Дата последней модификации: 17.12.2020
Описание: Решение задачи №44 Практикума №1
Описание: Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.
# Версия Python: 3.9
"""

import random
import numpy as np

N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0,N)]
print(A)
Ao = []
Ap = []

for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
sumAo = np.size(Ao)
sumAp = np.size(Ap)
Q = sumAo-sumAp
W = sumAp - sumAo
print(sumAo)
print(sumAp)

if sumAo == sumAp:
    print("Количество отрицательных и положительных элементов массива равно")
if sumAo > sumAp:
    A.append([random.randint(1,10) for i in range(0,Q)])
if sumAp > sumAo:
    A.append([random.randint(-1, -10) for i in range(0,W)])
    
print(A)
