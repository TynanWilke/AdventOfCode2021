#!/usr/bin/python3

import copy
import sys

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
coords = [list(map(int, line.split(','))) 
          for line in lines if line and 'fold' not in line]
folds = []
for line in lines:
    if 'fold' not in line:
        continue
    fold, line = line.split(' ')[2].split('=')
    folds.append((fold, int(line)))
print('coords', coords)
print('folds', folds)

for fold, line in folds:
    print('fold', fold)
    print('line', line)
    new_coords = []
    for x, y in coords:
        print('x', x)
        print('y', y)
        if fold == 'x':
            if x > line:
                x -= 2*(x - line)
        else:
            if y > line:
                y -= 2*(y - line)
        print('fold x', x)
        print('fold y', y)
        new_coords.append((x, y))
    coords = new_coords
    print('coords', coords)
dots = set(coords)
print('dots', dots)
print('count', len(dots))
for y in range(0, 1 + max([point[1] for point in coords])):
    for x in range(0, 1 + max([point[0] for point in coords])):
        if (x, y) in coords:
            sys.stdout.write('#')
        else:
            sys.stdout.write('.')
    sys.stdout.write('\n')

