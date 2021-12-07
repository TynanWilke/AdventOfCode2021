#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    crabs = list(map(int, lines[0].split(',')))
    print(crabs)

    min_move = min([(sum(abs(crab - i) for crab in crabs), i) 
                    for i in range(min(crabs), max(crabs) + 1)])
    print(min_move)
