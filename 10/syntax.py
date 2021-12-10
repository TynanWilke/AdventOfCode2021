#!/usr/bin/python3

closer = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
    }

scores = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
    }

total = 0
for line in open('test.txt'):
    opened = []
    for char in list(line.strip()):
        if char in closer.values():
            opened.append(char)
        elif not opened or opened.pop() != closer[char]:
            total += scores[char]
            break
print(total)
