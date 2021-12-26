#!/usr/bin/python3

import sys

with open('input.txt') as f:
    lines = [line.strip() for line in f]
print(lines)

east = set(
        [(x, y) 
        for x in range(0, len(lines[0])) 
        for y in range(0, len(lines))
        if lines[y][x] == '>'])
print('east', east)
south = set(
        [(x, y) 
        for x in range(0, len(lines[0])) 
        for y in range(0, len(lines))
        if lines[y][x] == 'v'])
print('south', south)

def print_board():
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            point = (x, y)
            if point in east:
                sys.stdout.write('>')
                continue
            if point in south:
                sys.stdout.write('v')
                continue
            sys.stdout.write('.')
        sys.stdout.write('\n')

i = 1
while True:
    east_movable = dict()
    for old_point in east:
        x, y = old_point
        if x != len(lines[0]) - 1:
            new_point = (x + 1, y)
        else:
            new_point = (0, y)
        if new_point in east \
                or new_point in south:
            continue
        east_movable[old_point] = new_point
    for old_point, new_point in east_movable.items():
        east.discard(old_point)
        east.add(new_point)

    south_movable = dict()
    for old_point in south:
        x, y = old_point
        if y != len(lines) - 1:
            new_point = (x, y + 1)
        else:
            new_point = (x, 0)
        if new_point in east \
                or new_point in south:
            continue
        south_movable[old_point] = new_point
    for old_point, new_point in south_movable.items():
        south.discard(old_point)
        south.add(new_point)

    if not east_movable and not south_movable:
        break
    i += 1
    #print_board()
print('step', i)
