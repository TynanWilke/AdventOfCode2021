#!/usr/bin/python3

hor = 0
dep = 0
aim = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip();
        d, x = line.split()
        x = int(x)
        if d == "up":
            aim -= x
        elif d == "down":
            aim += x
        elif d == "forward":
            hor += x
            dep += aim*x
print(hor, dep, aim)
print(hor*dep)

