#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Advanced calculator."""


import math
import operator


CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "t": math.tau,
}
BINARY_OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}
PREFIX_OPERATORS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tg": math.tan,
    "arcsin": math.asin,
    "arccos": math.acos,
    "ln": math.log,
}
POSTFIX_OPERATORS = {
    "!": math.factorial,
}
PRIORITIES = {
    "(": 0,
    ")": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}


def is_brackets_agreed(expression: list) -> bool:
    amount_of_brackets = 0
    for el in expression:
        if el == "(":
            amount_of_brackets += 1
        elif el == ")":
            amount_of_brackets -= 1

    if amount_of_brackets == 0:
        return True

    return False


def is_known_characters(expression: list) -> bool:
    for el in expression:
        if el not in [i for i in CONSTANTS.keys()] +\
                [i for i in BINARY_OPERATORS.keys()] +\
                [i for i in PREFIX_OPERATORS.keys()] + [i for i in POSTFIX_OPERATORS.keys()] +\
                ["(", ")"] and not el.isdigit():
            return False

    return True


def calculate(reverse_polish_notation: list) -> float:
    stack = []
    for el in reverse_polish_notation:
        if el.isdigit():
            stack.append(float(el))

        elif el in BINARY_OPERATORS:
            first_operand, second_operand = stack.pop(-2), stack.pop(-1)
            stack.append(BINARY_OPERATORS[el](first_operand, second_operand))

        elif el in PREFIX_OPERATORS:
            stack.append(PREFIX_OPERATORS[el](stack.pop(-1)))

        elif el in POSTFIX_OPERATORS:
            stack.append(POSTFIX_OPERATORS[el](stack[-1]))

        elif el in CONSTANTS:
            stack.append(CONSTANTS[el])

    return stack.pop()


def check_for_correctness(func):
    def inner(expression):
        if is_brackets_agreed(expression) and is_known_characters(expression):
            return calculate(func(expression))
        else:
            if not is_brackets_agreed(expression):
                return "Не согласованы скобки!"
            elif not is_known_characters(expression):
                return "Вы ввели неизвестные символы!"

    return inner


@check_for_correctness
def convert_to_rpn(expression: list) -> list:
    stack = []
    reverse_polish_notation = []

    for el in expression:
        if el.isdigit() or el in POSTFIX_OPERATORS or el in CONSTANTS:
            reverse_polish_notation.append(el)

        elif el in PREFIX_OPERATORS or el == "(":
            stack.append(el)

        elif el == ")":
            while stack[-1] != "(":
                reverse_polish_notation.append(stack.pop())
            stack.pop()

        elif el in BINARY_OPERATORS:
            if len(stack) != 0:
                while stack[-1] in PREFIX_OPERATORS or PRIORITIES[stack[-1]] >= PRIORITIES[el]:
                    reverse_polish_notation.append(stack.pop())
                    if not stack:
                        break
            stack.append(el)

    reverse_polish_notation.extend(reversed(stack))

    return reverse_polish_notation


def parse(expression: str) -> list:
    array = []
    operand = ""

    for index, el in enumerate(expression):
        if el.isalpha() or el.isdigit():
            operand += el

        elif el != " ":
            if operand != "":
                array.append(operand)
                operand = ""

            elif el == "*" and array[-1] == "*":
                array[-1] = "^"
                continue

            elif el == "-" and index == 0 or array[-1] == "(":
                array.append("0")

            array.append(el)

        if index == len(expression) - 1 and operand != "":
            array.append(operand)

    return array


if __name__ == "__main__":
    repeat = True

    while repeat:
        user_input = input("\nEnter the expression ('q' - to quit): ")

        if user_input != "q":
            user_input = parse(user_input)
            reverse_polish_notation = convert_to_rpn(user_input)
            print(reverse_polish_notation)

        else:
            repeat = False
