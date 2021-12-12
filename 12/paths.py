#!/usr/bin/python3

import copy

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
conns = [line.split('-') for line in lines]

def search(curr_path, small_caves):
    cave = curr_path[-1]
    if cave == 'end':
        return [copy.copy(curr_path)]
    if cave in small_caves:
        return [None]
    if cave == cave.lower():
        small_caves.add(cave)

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
        small_caves.remove(cave)
    return paths
paths = search(['start'], set())
print(len(paths))
