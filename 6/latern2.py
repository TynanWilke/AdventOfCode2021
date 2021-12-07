#!/usr/bin/python3

from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [line for line in f]
    fishes = list(map(int, lines[0].strip().split(',')))
    groups = defaultdict( \
            lambda: 0, \
            [(i, len([fish for fish in fishes if fish == i])) for i in set(fishes)])
    for i in range(0, 256):
        groups = defaultdict( \
                lambda: 0,    \
                [(i - 1, groups[i]) for i in set(groups.keys())])
        print("After %d day: %s" % (i + 1, ','.join(map(str, sorted(groups.items())))))
        if i == 255:
            break
        
        if 0 in groups:
            new_fish = groups[0] 
            groups[7] += new_fish
            groups[9] = new_fish
            del groups[0]
    print(sum(groups.values()))
