#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Prints flags."""


def print_flags(n: int, flag: list):
    for i in range(4):
        for j in range(n):
            if i == 1:
                print(flag[i].replace("1", str(j + 1)), end=" ")
            else:
                print(flag[i], end=" ")
        print("\n", end="")


if __name__ == "__main__":
    n = None
    while n not in range(1, 10):
        n = int(input("Enter amount of flags [1-9]: "))

    flag = [
        "+___",
        "|1 /",
        "|__\\",
        "|   ",
    ]

    print_flags(n, flag)
