#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Describes amount of likes."""


def likes(*arr: str) -> str:
    if len(arr) == 0:
        return "no one likes this"
    elif len(arr) == 1:
        return "{} likes this".format(*arr)
    elif len(arr) == 2:
        return "{} and {} like this".format(*arr)
    elif len(arr) == 3:
        return "{}, {} and {} like this".format(*arr)
    else:
        return "{}, {} and {} others like this".format(*arr[:2], len(arr)-2)


if __name__ == "__main__":
    amount_of_likes = likes("Alex", "Jacob", "Mark", "Max")
    print(amount_of_likes)