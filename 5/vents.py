#!/usr/bin/python3

import sys
from collections import defaultdict

with open("input.txt", 'r') as f:
    points = defaultdict(lambda: 0)
    for line in f:
        line = line.strip()
        print(line)
        start, _, end = line.split()
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        print(x1)
        print(x2)
        print(y1)
        print(y2)
        new_points = []
        if x1 == x2:
            new_points = [(x1, i) for i in range(y1, y2 + 1)]
            new_points += [(x1, i) for i in range(y2, y1 + 1)]
        if y1 == y2:
            new_points = [(i, y1) for i in range(x1, x2 + 1)]
            new_points += [(i, y1) for i in range(x2, x1 + 1)]
        new_points = sorted(list(set(new_points)))
        print(new_points)
        for new_point in new_points:
            points[new_point] += 1
        sys.exit(1)
    for i in range(0, max(map(lambda x: x[0], points.keys())) + 1):
        for j in range(0, max(map(lambda x: x[1], points.keys())) + 1):
            sys.stdout.write(str(points[(i, j)]) + ' ')
        sys.stdout.write('\n')

    v = sum([cnt >=2 for cnt in points.values()])
    print(v)
                
