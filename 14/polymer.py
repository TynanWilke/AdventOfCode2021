#!/usr/bin/python3

import copy
import sys

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
template = lines[0]
rules = [line.split(' -> ') for line in lines[1:] if line]

for i in range(0, 10):
    bonds = [(i, template[i]+template[i+1]) for i in range(0, len(template) - 1)]
    insertions = []
    for pair, element in rules:
        for i, bond in bonds:
            if bond == pair:
                insertions.append((i, element))
    for i, element in sorted(insertions, reverse=True):
        template = template[0:i + 1] + element + template[i + 1:]
counts = [(template.count(element), element) for element in set(template)]
counts.sort()
print('ans', counts[-1][0] - counts[0][0])
