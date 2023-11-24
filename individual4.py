#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == "__main__":
    n = int(input("Введите значение n для функции Бесселя первого рода: "))
    x = float(input("Введите значение x: "))

    result = 0.0
    terms = 50

    for k in range(terms):
        numerator = ((-(x ** 2) / 4) ** k) / (math.factorial(k) * math.factorial(k + n))
        result += numerator

    bessel_value = result * (x / 2) ** n
    print(bessel_value)
