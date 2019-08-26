#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Returns prime numbers."""


def is_prime(number: int) -> bool:
    """
    Function returns True if number is prime, and False if number is not prime.
    """
    if number == 2:
        return True

    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            if i == number - 1:
                return True
            continue


def get_prime_number():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


if __name__ == "__main__":
    gen_prime = get_prime_number()

    for i in range(5):
        print(next(gen_prime), end='\t')
