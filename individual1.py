#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь"]

    c = int(input("Введите целое число C, такое что |C| < 9: "))

    if c < 0:
        sign = "отрицательное"
        c = abs(c)
    else:
        sign = "положительное"

    word_form = words[c]
    print(f"Словесная форма числа {c}: {sign} {word_form}")
