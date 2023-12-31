# ДОМАШНЕЕ ЗАДАНИЕ 5

# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input('Введите возводимое в степень число А: '))
# b = int(input('Введите значение степени - число B: '))

# def f(a, b):     # задаем основание рекурсии - число a и степень - число b
#     if b == 1:   # надо обязательно указывать базис рекурсии (ограничение снизу,
#                  #     т.к. идем от большого к малому)
#         return a
#     if b != 1:
#         return a * f(a, b - 1)  # вывод 

# print(f(a, b))

# Вариант 2
# print(pow(a, b))
# print(a ** b)

# ---------------------------------

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

def summa(a, b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)
print(summa(a - 1, b + 1))

# Вариант 2
# def sintez(a, b):
#     return a + b
# print(sintez(a, b))

# Вариант 3
# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
# print(summa(a, b))
# ---------------------