#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Ceaser's code."""


def check_the_shift(shift: int) -> int:
    if ALPHABET != None and shift > len(ALPHABET):
        return shift % len(ALPHABET)
    return shift


def create_alphabet(text: str) -> str:
    if get_order_sign(text) in range(97, 123):
        return "".join([chr(i) for i in range(ord("a"), ord("a")+26)])

    elif get_order_sign(text) in range(1072, 1104):
        return "".join([chr(i) for i in range(ord("а"), ord("а")+32)])


def encode(text: str, shift: int, decode=False) -> str:
    encoded_text = ""

    for index, sign in enumerate(text.lower()):
        if not sign.isalpha():
            encoded_text += sign
            continue

        if decode:
            index_of_encoded_sign = ALPHABET.index(sign) - shift
        else:
            index_of_encoded_sign = ALPHABET.index(sign) + shift
            if index_of_encoded_sign > len(ALPHABET) - 1:
                index_of_encoded_sign -= len(ALPHABET)

        if text[index].isupper():
            encoded_text += ALPHABET[index_of_encoded_sign].upper()
        else:
            encoded_text += ALPHABET[index_of_encoded_sign]

    return encoded_text


def get_order_sign(text: str) -> int:
    for sign in text.lower():
        if sign.isalpha():
            return ord(sign)
    return None


if __name__ == "__main__":
    while True:
        text = input("Enter your text here: ")
        ALPHABET = create_alphabet(text)
        shift = check_the_shift(int(input("Enter a shift: ")))
        encoded_text = encode(text, shift)
        decoded_text = encode(encoded_text, shift, decode=True)

        print(text, encoded_text, sep=" -> ", end="\n\n")
        print(encoded_text, decoded_text, sep=" -> ", end="\n\n")

        _exit = input("Press 'q' - to quit: ")
        if _exit == "q":
            break
