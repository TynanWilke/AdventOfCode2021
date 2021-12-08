#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    cnt = 0
    for line in lines:
        segments, outputs = [_.split() for _ in line.split('|')]
        cnt += len([output for output in outputs if len(output) in (2, 4, 3, 7)])
    print(cnt)

