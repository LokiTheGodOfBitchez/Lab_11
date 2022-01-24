#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multi():
    number = int(input("Введите число: "))
    result = 1
    if number == 0:
        return None
    while number != 0:
        result *= number
        number = int(input("Введите число: "))
    return result


if __name__ == '__main__':
    print(f"Вызов функции и ее результата = {multi()}")
