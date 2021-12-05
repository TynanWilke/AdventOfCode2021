#!/usr/bin/python3

import collections

ones = collections.defaultdict(lambda: 0)
with open('input.txt', 'r') as f:
    for l, line in enumerate(f):
        line = line.strip()
        for i, c in enumerate(line):
            if c == '1':
                ones[i] += 1

    gamma = str()
    for i in range(max(ones.keys()) + 1):
        if ones[i] > l/2:
            gamma += '1'
        else:
            gamma += '0'
    gammav = sum(int(c)*pow(2, i) for i, c in enumerate(reversed(gamma)))
    epsilonv = sum((1 if int(c) == 0 else 0)*pow(2, i) for i, c in enumerate(reversed(gamma)))
    print(gammav*epsilonv)
