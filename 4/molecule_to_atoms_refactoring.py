#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Parsing the chemical formula of molecules."""
import re

from collections import Counter


def parse_molecule(molecule: str) -> dict:
    brackets = re.search(r'[({\[]\w*[)}\]]\d?', molecule)

    if brackets:
        brackets = brackets[0]
        if brackets[-1] not in ')]}':
            coef = int(brackets[-1])
            molecule = molecule.replace(brackets, brackets[1:-2] * coef)
        else:
            molecule = molecule.replace(brackets, brackets[1:-1])
    i = 0
    while i < len(molecule):
        if molecule[i].isdigit():
            if molecule[i - 1].islower():
                molecule = molecule.replace(molecule[i], molecule[i - 2: i] * (int(molecule[i]) - 1), 1)
            else:
                molecule = molecule.replace(molecule[i], molecule[i - 1] * (int(molecule[i]) - 1), 1)
        i += 1

    atoms = re.findall(r'[A-Z][a-z]?', molecule)
    result = Counter(atoms)

    return dict(result)


if __name__ == "__main__":
    print(parse_molecule('Mg2O2H2'))
    print(parse_molecule('Mg3(OH)2'))
