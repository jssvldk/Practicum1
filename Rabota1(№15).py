Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
Имя проекта: Rabota1
Номер версии: 1.0
Имя файла: Rabota1(№15).py
Автор: 2020 © В.А.Шаровский, Челябинск
Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 15.12.2020
Дата последней модификации: 15.12.2020
Описание: Решение задачи №15 Практикума №1
Описание: Дан номер места в плацкартном вагоне. Определить, какое это место: верхнее или нижнее, в купе или боковое.
# Версия Python: 3.9
"""

Num = int(input("Укажите номер места в плацкартном вагоне:"))
if (Num > 60):
    print("Такого номера не существует, проверьте данные:")
elif (Num > 0 and Num < 35):
    print("Ваше место в купе")
else:
    print("Ваше место - боковое")
if (Num % 2 == 0):
    print("верхнее")
else:
    print("нижнее")