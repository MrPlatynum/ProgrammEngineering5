#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == "__main__":
    n = int(input("Введите значение n для функции Бесселя первого рода: "))
    x = float(input("Введите значение x: "))

    result = 0.0
    terms = 50

    a = 1 / math.factorial(n)
    for k in range(terms):
        result += a
        a = a * (-(x ** 2) / 4) / ((k + 1) * (k + n + 1))

    bessel_value = result * (x / 2) ** n
    print(bessel_value)
