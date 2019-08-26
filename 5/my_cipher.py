#!/usr/bin/python3.7.3
# -*- coding: utf-8 -*-
"""My cipher."""


import random
import string


SIGNS = string.printable


def convert_to_indexes(text: str) -> list:
    return [SIGNS.index(sign) for sign in text]


def encrypt_text(text: str, key: list, decode=False) -> str:
    encrypted_text = ""

    if decode == True:
        for index, el in enumerate(text.split()):
            encrypted_text += SIGNS[int(el) ^ key[index]]
    else:
        indexes_of_signs = convert_to_indexes(text)

        for index, el in enumerate(indexes_of_signs):
            encrypted_text += str(el ^ key[index]) + " "

    return encrypted_text


def get_random_key(length: int) -> list:
    return [random.choice(range(len(SIGNS))) for i in range(length)]


if __name__ == "__main__":
    while True:
        text = input("\nEnter the text to encode them [q - quit]: ")

        if text == "q":
            break

        hash_of_text = hash(text)
        text += "\nhash: " + str(hash_of_text)
        key = get_random_key(len(text))
        encoded_text = encrypt_text(text, key)
        decoded_text = encrypt_text(encoded_text, key, decode=True)

        print("\nrandom key:", key)
        print("encoded text:", encoded_text)
        print("decoded text:", decoded_text)