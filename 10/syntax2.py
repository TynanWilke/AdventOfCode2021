#!/usr/bin/python3

closer = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
    }
opener = dict((y, x) for x, y in closer.items())

scores = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4 
    }

totals = []
for line in open('input.txt'):
    opened = []
    bad = False
    for char in list(line.strip()):
        if char in closer.values():
            opened.append(char)
        elif opened[-1] != closer[char]:
            bad = True
            break
        else:
            opened.pop()
    if bad or not opened:
        continue
    score = 0
    closers = list(reversed([opener[char] for char in opened]))
    for char in closers:
        score *= 5
        score += scores[char]
    totals.append(score)
totals.sort()
print(totals[int(len(totals)/2)])
