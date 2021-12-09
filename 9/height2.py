#!/usr/bin/python3

import sys
from collections import defaultdict
from functools import reduce

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    heights = [list(map(int, [c for c in line])) for line in lines]
    def print_rect(rect):
        for r in range(0, len(rect)):
            for c in range(0, len(rect[r])):
                sys.stdout.write(str(rect[r][c]) + ' ')
            sys.stdout.write('\n')
    print_rect(heights)

    basins = []
    def nearby(r, c, found_points):
        found_points = list(set(found_points))
        points = [(row, col) 
                  for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                      if row >= 0 and row < len(heights) \
                              and col >= 0 and col < len(heights[row]) \
                              and heights[row][col] != 9 \
                              and (row, col) not in found_points]
        found_points += points
        for point in points:
            found_points += nearby(point[0], point[1], found_points)
        return set(found_points)
    for r in range(0, len(heights)):
        for c in range(0, len(heights[r])):
            if heights[r][c] == 9:
                continue
            found = False
            points = nearby(r, c, [])
            for point in points:
                for basin in basins:
                    if point in basin:
                        basin.add((r, c))
                        found = True
            if not found:
                basins.append(set([(r, c)]))
    max3 = sorted(basins, key=len)[-3:]
    for basin in max3:
        for r, c in basin:
            heights[r][c] = 'X'
    print_rect(heights)

    p = reduce(lambda x, y: x * y, [len(x) for x in max3])
    print(p)

