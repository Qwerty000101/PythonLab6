#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = input("Введите предложение:\n").split()

    if len(n) > 3:
        print("Предложение содержит больше трёх слов")
    else:
        print("Предложение содержит не больше трёх слов.")