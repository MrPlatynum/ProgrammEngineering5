#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    if a > 0:
        print(f"x < {x1} или x > {x2}")
    else:
        print(f"{x1} < x < {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    if a > 0:
        print(f"x = {x}")
    else:
        print("Нет действительных корней")
else:
    print("Пустое множество")
