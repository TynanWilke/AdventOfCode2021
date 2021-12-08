#!/usr/bin/python3

import sys
import copy

digits = {}
digits["abcefg"] = 0
digits["cf"] = 1
digits["acdeg"] = 2
digits["acdfg"] = 3
digits["bcdf"] = 4
digits["abdfg"] = 5
digits["abdefg"] = 6
digits["acf"] = 7
digits["abcdefg"] = 8
digits["abcdfg"] = 9

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f]
    cnt = 0
    for line in lines:
        segments, outputs = [_.split() for _ in line.split('|')]
        segments = [''.join(sorted(segment)) for segment in segments]
        segments.sort(key=len)
        wires = dict([(c, set("abcdefg")) for c in set("abcdefg")])
        def print_wires(w):
            for c, opts in sorted(w.items()):
                print("%s: %s" % (c, ' '.join(sorted(list(opts)))))
        for segment in reversed(segments):
            matching_digits = [digit for digit in digits if len(digit) == len(segment)]
            if len(matching_digits) != 1:
                continue
            for digit in matching_digits:
                for c in digit:
                    wires[c] = wires[c].intersection(segment)
        #print_wires(wires)

        def solved(w):
            if any([len(opts) != 1 for opts in w.values()]):
                return False
            for digit in digits:
                mapped = ''.join(sorted([list(w[c])[0] for c in digit]))
                if mapped not in segments:
                    return False;
            return True
        def resolve(w):
            if solved(w):
                return w
            assert all(len(opts) > 0 for opts in w.values())
            for wire, opts in sorted([item for item in w.items() if len(item[1]) > 1], key=lambda x: len(x[1])):
                for opt in opts:
                    cw = copy.deepcopy(w)
                    cw[wire] = set([opt])
                    for remove_wire, remove_opts in cw.items():
                        if wire == remove_wire:
                            continue
                        remove_opts.discard(opt)
                    if any(len(remove_opt) == 0 for remove_opt in cw.values()):
                        continue
                    cw = resolve(cw)
                    if cw is not None:
                        return cw
            return None
        wires = resolve(wires)
        #print_wires(wires)
        wires = dict((list(opts)[0], wire) for wire, opts in wires.items())

        num = ''
        for output in outputs:
            digit = ''.join(sorted([wires[c] for c in output]))
            num += str(digits[digit])
        cnt += int(num)
    print(cnt)

