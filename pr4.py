#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input()


def test_input(string):
    return string.isdigit()


def str_to_int(string):
    return int(string)


def print_int(integer):
    print(integer)


def main():
    data = get_input()
    if test_input(data):
        print_int(str_to_int(data))


if __name__ == '__main__':
    main()
