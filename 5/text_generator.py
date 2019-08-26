#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Text generator."""


import random


def generate_the_text(start_word: str, amount_of_words: int, combinations: dict) -> str:
    generated_text = [start_word]

    while len(generated_text) < amount_of_words:
        if start_word == training_text[-1]:
            start_word = get_random_word(training_text)

        most_common_word = get_most_common_word(start_word, combinations)
        generated_text.append(most_common_word)
        start_word = most_common_word

    return " ".join(generated_text)


def get_most_common_word(start_word: str, combinations: dict) -> str:
    arr_of_words = []

    for word in combinations[start_word].keys():
        arr_of_words.append(word)

    return random.choice(arr_of_words)


def get_random_word(array: list) -> str:
    while True:
        start_word = random.choice(training_text[:-1])

        if start_word.isalpha():
            return start_word


def parse_text(text: str) -> list:
    array = []
    word = ""

    for index, el in enumerate(text.lower()):
        if el.isalpha():
            word += el

        elif el.isspace() and word != "":
            array.append(word)
            word = ""

        elif not el.isalpha() and not el.isspace():
            if len(word) > 0:
                array.append(word)
            word = ""
            array.append(el)

    if len(word) > 0:
        array.append(word)

    return array


def train(training_text: list) -> dict:
    combinations = {}

    for index, word in enumerate(training_text):
        if index == len(training_text) - 1:
            break

        next_word = training_text[index + 1]

        if word not in combinations.keys():
            combinations[word] = {next_word: 1}
        elif word in combinations.keys() and next_word not in combinations[word].keys():
            combinations[word][next_word] = 1
        elif word in combinations.keys() and next_word in combinations[word].keys():
            combinations[word][next_word] += 1

    return combinations


if __name__ == "__main__":
    filename = "training_text.txt.txt"

    with open(filename) as f:
        training_text = parse_text(f.read())

    combinations = train(training_text)
    start_word = get_random_word(training_text)
    amount_of_words = int(input("Enter an amount of words: "))
    generated_text = generate_the_text(start_word, amount_of_words, combinations)

    print("\nstart word:", start_word)
    print("\ngenerated text:\n", generated_text)
