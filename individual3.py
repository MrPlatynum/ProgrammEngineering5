#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = int(input("Введите значение a (количество фунтов): "))

    print("Вес в фунтах | Вес в килограммах")
    print("-" * 30)

    for pounds in range(1, a + 1):
        kilograms = pounds * 400 / 1000
        print(f"{pounds:^13} | {kilograms:^18.2f}")
