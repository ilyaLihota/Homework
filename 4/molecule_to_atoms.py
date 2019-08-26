#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
"""Molecule to atoms."""


def get_sub_molecule(molecule: list, atom: str) -> list:
    molecule_copy = molecule[molecule.index(atom) + 1:]
    sub_molecule = []
    count_parent = 1

    for el in molecule_copy:
        if el in "([{":
            count_parent += 1
        elif el in ")]}":
            count_parent -= 1

        if count_parent == 0:
            molecule.remove(el)
            break

        sub_molecule.append(el)
        molecule.remove(el)

    return sub_molecule


def parse_molecule(molecule):
    molecule = [i for i in molecule]
    element = ""
    array_of_elements = []
    atoms = {}

    for atom in molecule:
        if atom.isupper():
            if element != "":
                array_of_elements.append(element)
                atoms[atom] = 0
                atoms[atom] += 1
            if molecule.index(atom) == len(molecule) - 1:
                array_of_elements.append(atom)
            else:
                element = atom

        elif atom.islower():
            element += atom

        elif atom.isdigit():
            for i in range(int(atom)):
                if isinstance(element, str):
                    array_of_elements.append(element)
                elif isinstance(element, list):
                    array_of_elements.extend(element)
            element = ""

        if atom in "([{":
            if element != "":
                array_of_elements.append(element)

            sub_molecule = get_sub_molecule(molecule, atom)
            element = parse_molecule(sub_molecule)

    return array_of_elements


if __name__ == "__main__":
    molecule = "K4[ON(SO3)2]2"
    amount_of_atoms = {}
    array_of_elements = parse_molecule(molecule)

    for atom in array_of_elements:
        amount = array_of_elements.count(atom)
        amount_of_atoms[atom] = amount

    print(amount_of_atoms)
