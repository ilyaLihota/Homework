#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Memoization."""
from functools import wraps


def memoization(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        key = str(key)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return inner


@memoization
def add(a: int, b: int) -> str:
    return str(a + b)


@memoization
def acc(a, b, c):
    return a + b + c


if __name__ == "__main__":
    print(add(3, 4))
    print(add(3, 4))
    print(add(1, 2), "\n")

    print(acc(1, 2, 3))
    print(acc(4, 2, 8))
    print(acc(1, 2, 3), "\n")

    print(add(9, 11))
