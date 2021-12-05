#!/usr/bin/python3

import collections
import copy

with open('input.txt', 'r') as f:
    bits = []
    for l, line in enumerate(f):
        line = line.strip()
        bits.append(line)
    
    oxy_bits = copy.copy(bits)
    i = 0
    while True:
        ones = sum(int(bit[i]) for bit in oxy_bits)
        if ones >= len(oxy_bits)/2:
            oxy_bits = [bit for bit in oxy_bits if bit[i] == '1']
        else:
            oxy_bits = [bit for bit in oxy_bits if bit[i] == '0']
        i += 1
        if len(oxy_bits) == 1:
            break
        assert i != len(oxy_bits[0])

    co2_bits = copy.copy(bits)
    i = 0
    while True:
        ones = sum(int(bit[i]) for bit in co2_bits)
        if ones >= len(co2_bits)/2:
            co2_bits = [bit for bit in co2_bits if bit[i] == '0']
        else:
            co2_bits = [bit for bit in co2_bits if bit[i] == '1']
        i += 1
        if len(co2_bits) == 1:
            break
        assert i != len(co2_bits[0])

    oxyv = sum(int(c)*pow(2, i) for i, c in enumerate(reversed(oxy_bits[0])))
    co2v = sum(int(c)*pow(2, i) for i, c in enumerate(reversed(co2_bits[0])))
    print(oxyv*co2v)
