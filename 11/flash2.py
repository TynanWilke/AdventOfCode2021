#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
octopi = [[int(c) for c in line] for line in lines]

i = 0
while True:
    octopi = [[o + 1 for o in row] for row in octopi]
    flashed = []
    while True:
        need_flash = [(r, c) 
                      for r, row in enumerate(octopi) 
                      for c, o in enumerate(row) 
                      if o >= 10]
        if not need_flash:
            break
        for r, c in need_flash:
            if (r, c) in flashed:
                continue
            octopi[r][c] = 0
            flashed.append((r, c))

            for sr, sc in [(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]:
                if (sr, sc) in flashed:
                    continue
                if 0 <= sr < len(octopi) and 0 <= sc < len(octopi[0]):
                    octopi[sr][sc] += 1
    if all((r, c) in flashed 
           for r in range(0, len(octopi)) 
           for c in range(0, len(octopi[0]))):
        break
    i += 1

def print_octopi(rect):
    for row in rect:
        print(''.join(map(str, row)))
print_octopi(octopi)
print("step", i + 1)
