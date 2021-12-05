#!/usr/bin/python3

import sys
from collections import defaultdict

with open("input.txt", 'r') as f:
    points = defaultdict(lambda: 0)
    for line in f:
        line = line.strip()
        start, _, end = line.split()
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        new_points = []
        if x1 == x2:
            new_points = [(x1, i) for i in range(y1, y2 + 1)]
            new_points += [(x1, i) for i in range(y2, y1 + 1)]
        if y1 == y2:
            new_points = [(i, y1) for i in range(x1, x2 + 1)]
            new_points += [(i, y1) for i in range(x2, x1 + 1)]
        if abs(x1 - x2) == abs(y1 - y2):
            if y2 > y1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for i in range(0, abs(x1 - x2) + 1):
                x, y = x1 + i, y1 - i
                if x <= x2:
                    new_points.append((x, y))
                x, y = x2 + i, y2 + i
                if x <= x1:
                    new_points.append((x, y))
        new_points = sorted(list(set(new_points)))
        for new_point in new_points:
            points[new_point] += 1
    for i in range(0, max(map(lambda x: x[1], points.keys())) + 1):
        for j in range(0, max(map(lambda x: x[0], points.keys())) + 1):
            sys.stdout.write(str(points[(i, j)]) + ' ')
        sys.stdout.write('\n')
    v = sum([cnt >=2 for cnt in points.values()])
    print(v) 
