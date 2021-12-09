#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    heights = [list(map(int, [c for c in line])) for line in lines]
    print(heights)
    lows = []
    for r in range(0, len(heights)):
        for c in range(0, len(heights[r])):
            print(r)
            print(c)
            print(heights[r][c])
            bounds = []
            if r - 1 >= 0:
                bounds.append(heights[r-1][c])
            if r + 1 < len(heights):
                bounds.append(heights[r+1][c])
            if c - 1 >= 0:
                bounds.append(heights[r][c-1])
            if c + 1 < len(heights[r]):
                bounds.append(heights[r][c+1])
            print(bounds)
            if heights[r][c] < min(bounds):
                lows.append(heights[r][c])
    print(lows)
    print(sum(lows) + len(lows))
