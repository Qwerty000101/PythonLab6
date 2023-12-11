#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s_first = input("Введите первое предложение:\n").split()
    s_second = input("Введите второе предложение:\n").split()
    st = []
    
    for word in s_first:
        if word in st:
            continue
        else:
            st.append(word)

    for word in st:
        if s_second.count(word) != 0:
            print(f"Слово '{word}' входит во второе предложение")
        else:
            print(f"Слово '{word}' не входит во второе предложение")
    
    