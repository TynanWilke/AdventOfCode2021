#!/usr/bin/python3

import copy
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
conns = [line.split('-') for line in lines]

def search(curr_path, small_caves):
    cave = curr_path[-1]
    if cave == 'end':
        return [copy.copy(curr_path)]
    if small_caves['start'] > 1:
        return [None]
    if small_caves[cave] > 0 \
            and any([v > 1 for v in small_caves.values()]):
        return [None]
    if cave == cave.lower():
        small_caves[cave] += 1

    avail_conns = [conn if conn[0] == cave else list(reversed(conn))
                   for conn in conns 
                   if cave in conn]
    paths = []
    for a, b in avail_conns:
        curr_path.append(b)
        next_paths = search(curr_path, small_caves)
        for next_path in next_paths:
            if next_path is not None:
                paths.append(next_path)
        curr_path.pop()

    if cave in small_caves:
        small_caves[cave] -= 1
    return paths
paths = search(['start'], defaultdict(lambda: 0))
print(len(paths))

