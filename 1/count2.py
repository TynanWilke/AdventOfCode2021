#!/usr/bin/python3

import sys
import collections

ranges = collections.defaultdict(list)
for i, line in enumerate(sys.stdin):
    depth = int(line.strip())
    ranges[i].append(depth)
    if i - 1 >= 0:
        ranges[i - 1].append(depth)
    if i - 2 >= 0:
        ranges[i - 2].append(depth)
    print(ranges)
cnt = 0
for i in range(max(ranges.keys())):
    print(ranges[i], sum(ranges[i]))
    print(ranges[i + 1], sum(ranges[i + 1]))
    if sum(ranges[i + 1]) > sum(ranges[i]):
        cnt += 1
        print("INC!")
print(cnt)
