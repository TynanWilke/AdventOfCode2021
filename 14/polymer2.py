#!/usr/bin/python3

import copy
import sys
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
template = lines[0]
rules = dict(line.split(' -> ') for line in lines[1:] if line)

pairs = [template[i]+template[i+1] for i in range(0, len(template) - 1)]
bonds = defaultdict(lambda: 0)
for pair in pairs:
    bonds[pair] += 1
for i in range(0, 40):
    for pair, count in copy.copy(bonds).items():
        if pair not in rules:
            continue
        element = rules[pair]
        bonds[pair[0]+element] += count
        bonds[element + pair[1]] += count
        bonds[pair] -= count
counts = defaultdict(lambda: 0)
for pair, count in bonds.items():
    counts[pair[0]] += count
    counts[pair[1]] += count
counts[template[0]] += 1
counts[template[-1]] += 1
counts = [int(i/2) for i in counts.values()]
counts.sort()
print('ans', counts[-1] - counts[0])
