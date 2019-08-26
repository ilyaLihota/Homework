#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Typing decorator."""


import inspect


def typed(strict=False):
    def outer(func):
        def inner(*args, **kwargs):
            annotations = func.__annotations__
            argspec = inspect.getfullargspec(func).args
            typed_args = dict(zip(argspec, args))
            converted_args = []

            if annotations == {}:
                return func(*args, **kwargs)

            for name, value in typed_args.items():
                if strict and not isinstance(value, annotations[name]):
                    raise TypeError(
                        "`{function_name}` argument `{name}` required to be a `{type}` instance.\n"
                        "Got `{wrong_type}` instance.".format(
                            function_name=func.__name__,
                            name=name,
                            type=annotations[name].__name__,
                            wrong_type=type(value).__name__
                        )
                    )

                elif not isinstance(value, annotations[name]):
                    if annotations[name].__name__ == "int":
                        converted_args.append(int(value))

                    elif annotations[name].__name__ == "float":
                        converted_args.append(float(value))

                    elif annotations[name].__name__ == "str":
                        converted_args.append(str(value))

                    elif annotations[name].__name__ == "bool":
                        converted_args.append(bool(value))
                else:
                    converted_args.append(value)

            if annotations["return"].__name__ == "int":
                return int(func(*converted_args, **kwargs))
            elif annotations["return"].__name__ == "float":
                return float(func(*converted_args, **kwargs))
            elif annotations["return"].__name__ == "str":
                return str(func(*converted_args, **kwargs))
            elif annotations["return"].__name__ == "bool":
                return bool(func(*converted_args, **kwargs))
        return inner
    return outer


@typed()
def add(a: int, b: int) -> str:
    return a + b


@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()


@typed()
def acc(a, b, c):
    return a + b + c


if __name__ == "__main__":
    print(add("3", "5"))
    print(add(2.35, True))

    print(convert_upper("abc"))
    # print(convert_upper(5))

    print(acc('a', 'b', 'c'))
    print(acc(5, 6, 7))
    print(acc(0.1, 0.2, 0.4))
