#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = input("Введите текст:\n")

    numbers_str = " ".join(c for c in n if c.isdigit()).split()
    numbers = [int(item) for item in numbers_str]

    print(f"Сумма: {sum(numbers)}\nМаксимальная цифра: {max(numbers)} ")
    