#!usr/bin/python3.5
# -*- coding: utf-8 -*-
"""Fraction."""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError("You try to divide by zero!")

    def __repr__(self):
        self.reduce_the_fraction()
        return "{numerator}/{denominator}".format(
            numerator=self.numerator,
            denominator=self.denominator)

    def __add__(self, other):
        return Fraction(
            self.numerator*other.denominator+other.numerator*self.denominator,
            self.denominator*other.denominator)

    def __sub__(self, other):
        return Fraction(
            self.numerator*other.denominator-other.numerator*self.denominator,
            self.denominator*other.denominator)

    def __mul__(self, other):
        return Fraction(
            self.numerator*other.numerator,
            self.denominator*other.denominator)

    def __truediv__(self, other):
        return Fraction(
            self.numerator*other.denominator,
            self.denominator*other.numerator)

    def reduce_the_fraction(self):
        for el in range(self.get_greatest(), 0, -1):
            if self.numerator % el == 0 and self.denominator % el == 0:
                self.numerator //= el
                self.denominator //= el

    def get_greatest(self):
        if self.numerator > self.denominator:
            return self.numerator
        return self.denominator


if __name__ == "__main__":
    fraction1 = Fraction(4, 5)
    print(fraction1 + Fraction(1, 8))
    print(fraction1 - Fraction(1, 8))
    print(fraction1 * Fraction(1, 8))
    print(Fraction(9, 12) / Fraction(1, 8))
    print(Fraction(40, 70))
