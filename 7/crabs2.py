#!/usr/bin/python3

with open('test.txt', 'r') as f:
    lines = [line.strip() for line in f]
    crabs = list(map(int, lines[0].split(',')))
    print(crabs)

    def cost(i):
        return sum(range(1, i + 1))
    min_move = min([(sum(cost(abs(crab - i)) for crab in crabs), i) 
                    for i in range(min(crabs), max(crabs) + 1)])
    print(min_move)
