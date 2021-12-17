#!/usr/bin/python3
import re
import sys

with open('input.txt') as f:
    lines = [line.strip() for line in f]
m = re.search('target area: x=([-0-9]*)\.\.([-0-9]*), y=([-0-9]*)..([-0-9]*)', str(lines[0]))
xr = [int(m.group(1)), int(m.group(2))]
yr = [int(m.group(3)), int(m.group(4))]
print('xr', xr)
print('yr', yr)

hits = 0
for xv in range(1, max(xr) + 1):
    for yv in range(min(yr), -min(yr) + 1):
        probe = [0, 0]
        start_xv = xv
        start_yv = yv
        step = 0
        while probe[1] >= min(yr) \
                and probe[0] <= max(xr):
            step += 1
            probe[0] += start_xv
            probe[1] += start_yv
            if start_xv != 0:
                start_xv -= 1
            start_yv -= 1
            
            if xr[0] <= probe[0] <= xr[1] \
                    and yr[0] <= probe[1] <= yr[1]:
                hits += 1
                break
print('hits', hits) 
