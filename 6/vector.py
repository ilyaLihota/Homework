#!usr/bin/python3.5
# -*- coding: utf-8 -*-
"""Vector."""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __eq__(self, other):
        if len(self.__dict__["components"]) == len(other.__dict__["components"]):
            return True
        else:
            raise TypeError("Unsupported operands error -\
                Vectors must be the same dimension")

    def __repr__(self):
        return "{0}: {1}".format(Vector.__name__, self.components)

    def is_valid_type(func):
        def inner(*args, **kwargs):
            if isinstance(args[-1], Vector):
                return func(*args, **kwargs)
            else:
                raise TypeError("Required {right_type} type object,\
                    but got {wrong_type} type.".format(
                        right_type=Vector, wrong_type=type(args[-1])))
        return inner

    @is_valid_type
    def __add__(self, other):
        if self == other:
            return Vector([key+value
                for key, value
                in dict(zip(self.components, other.components)).items()])

    @is_valid_type
    def __sub__(self, other):
        if self == other:
            return Vector([key-value
                for key, value
                in dict(zip(self.components, other.components)).items()])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([el*other for el in self.components])
        else:
            if self == other:
                return Vector(self.components[1]*other.components[-1] -
                              self.components[-1]*other.components[1],
                              self.components[-1]*other.components[0] -
                              self.components[0]*other.components[-1],
                              self.components[0]*other.components[1] -
                              self.components[1]*other.components[0])

    @is_valid_type
    def __matmul__(self, other):
        return sum([key*value
            for key, value
            in dict(zip(self.components, other.components)).items()])


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(9, 2)
    print(v1)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(v1 @ v2)
