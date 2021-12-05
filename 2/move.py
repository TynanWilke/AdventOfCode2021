#!/usr/bin/python3

hor = 0
dep = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip();
        print(line)
        d, x = line.split()
        x = int(x)
        if d == "up":
            dep -= x
        elif d == "down":
            dep += x
        elif d == "forward":
            hor += x
        print(hor, dep)
print(hor, dep)
print(hor*dep)

