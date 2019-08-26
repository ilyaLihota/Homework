# 0.Код спарсит формулы только с одним уровнем вложенности.
#   Чтобы парсить без ограничений по уровням вложенности, нужно применять рекурсию.
#   Возможно, сработают корутины с использованием стека.
# 1.Нет указаний интерпретатору.
#!/usr/bin/python
# -*- coding: utf-8 -*-
# 2.Нет описания файла.
import re
# 3.Между полными и частичными импортами - пустая строка.
from collections import Counter


# 4.Нет аннотации типа возвращаемого значения.
def parse_molecule(molecule: str):
    # 5.Переменная счетчик объявлена рано, лучше объявить сразу перед циклом while,
    #   чтобы явно указать к камоу блоку кода он относится.
    i = 0
    brackets = re.search(r'[({\[]\w*[)}\]]\d?', molecule)

    if brackets:
        brackets = brackets[0]
        if brackets[-1] not in ')]}':
            coef = int(brackets[-1])
            molecule = molecule.replace(brackets, brackets[1:-2] * coef)
        else:
            molecule = molecule.replace(brackets, brackets[1:-1])

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
