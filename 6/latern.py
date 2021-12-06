#!/usr/bin/python3

with open('input.txt', 'r') as f:
    lines = [line for line in f]
    fishes = list(map(int, lines[0].strip().split(',')))
    print(fishes)
    for i in range(0, 80):
        fishes = [fish - 1 if fish != 0 else 6 for fish in fishes]
        print("After %d day: %s" % (i + 1, ','.join(map(str, fishes))))
        print(len(fishes))
        fishes += [9 for fish in fishes if fish == 0]
