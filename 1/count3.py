#!/usr/bin/python3

import sys

cnt = 0
last = None
for i, line in enumerate(sys.stdin):
    depth = int(line.strip())
    if last != None and depth > last:
        cnt++
    last = depth

