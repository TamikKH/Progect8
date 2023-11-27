#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    Tuple = (tuple(map(int, input("Ведите строку чисел через пробел ").split())))
    flag = 0
    for i in range(0, len(Tuple)-1):
        if Tuple[i] > Tuple[i+1]:
            flag = flag + 1
            print(f"Первый неверный элемент = {Tuple[i]}")
            break
    if flag == 0:
        print("Кортеж отсортирован по возрастанию")
