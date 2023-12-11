#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n = input("Введите предложение:\n")

    res = n.find("а")
    if res == -1:
        print("Буква 'а' не найдена")
    else:
        print(f"Буква 'а' найдена. Порядковый номер: {res}")