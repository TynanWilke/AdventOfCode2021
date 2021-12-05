#!/usr/bin/python3

import sys

cnt = 0
last3 = []
curr3 = []
for i, line in enumerate(sys.stdin):
    depth = int(line.strip())
    if len(last3) == 3 and len(curr3) == 3 and sum(curr3) > sum(last3)
        cnt++
    last = depth

