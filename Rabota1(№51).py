"""
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№51).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 17.12.2020
Дата последней модификации: 17.12.2020
Описание: Решение задачи №51 Практикума №1
Описание: Заданы M строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.
# Версия Python: 3.9
"""

A = [A * 3 for A in 'abc']
print(A)
B = ['Hello', 'world!', 'qwe']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list.insert(0, '*')
        i = i + 1
        
print(B)
