#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi


def cylinder():

    def circle(rad):
        return pi * rad * rad

    r = int(input("Введите радиус: "))
    h = int(input("Введите высоту: "))
    choose = input("Площадь боковой поверхности цилиндра - a\n"
                   "Полная площадь цилиндра - b\n"
                   "a/b: ")
    if choose == 'a':
        print(f"Площадь боковой поверхности цилиндра = {2 * pi * r * h}")
    else:
        print(f"Полная площадь цилиндра = {2 * pi * r * h + 2 * circle(r)}")


if __name__ == '__main__':
    cylinder()
