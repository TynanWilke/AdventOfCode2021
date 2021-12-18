#!/usr/bin/python3
import sys
import ast
import re

with open('input.txt') as f:
    lines = [line.strip() for line in f]

def find_groups(pairs):
    lhs = ''
    rhs = pairs
    groups = []
    while True:
        g = re.findall('\[[0-9]+,[0-9]+\]', rhs)
        if not g:
            break
        match = g[0]
        lhs += rhs.split(match, 1)[0]
        rhs = rhs.split(match, 1)[1]
        groups.append((lhs, match, rhs))
        lhs += match
    return groups

def magnitude_of_pairs(pairs):
    rhs, lhs = pairs
    if not isinstance(rhs, int):
        rhs = magnitude_of_pairs(rhs)
    if not isinstance(lhs, int):
        lhs = magnitude_of_pairs(lhs)
    return 3*rhs + 2*lhs

def reduce_pairs(pairs):
    groups = find_groups(pairs)
    for lhs, g, rhs in groups:
        m = re.match('\[([0-9]+),([0-9]+)\]', g)
        a = int(m.group(1))
        b = int(m.group(2))
        # check explode
        nested = lhs.count('[') - lhs.count(']')
        if nested >= 4:
            # explode
            # find rightmost value in lhs
            m = re.match('(.*[^\d])(\d+)(?!\d+)(.*)', lhs)
            if m:
                explode_lhs = m.group(1)
                explode_d = int(m.group(2))
                explode_rhs = m.group(3)
                lhs = explode_lhs + str(explode_d + a) + explode_rhs
            # find leftmost value in rhs
            m = re.match('([^\d]+)([\d]+)(.*)', rhs)
            if m:
                explode_lhs = m.group(1)
                explode_d = int(m.group(2))
                explode_rhs = m.group(3)
                rhs = explode_lhs + str(explode_d + b) + explode_rhs
            pairs = lhs + '0' + rhs
            return (True, pairs)
    # check split 
    rs = re.findall('\d+', pairs)
    for r in rs:
        r = int(r)
        if r < 10:
            continue
        split_lhs, split_rhs = pairs.split(str(r), 1)
        if r % 2 == 0:
            ra = rb = int(r/2)
        else:
            ra = int(r/2)
            rb = ra + 1
        pairs = split_lhs + '[' + str(ra) + ',' + str(rb) + ']' + split_rhs
        return (True, pairs)
    return (False, pairs)

# reduce
pairs = lines[0]
for line in lines[1:]:
    pairs = '[' + pairs + ',' + line + ']'
    while True:
        did_reduce, pairs = reduce_pairs(pairs)
        if not did_reduce:
            break

pairs = ast.literal_eval(pairs)
print('magnitude_of_pairs', magnitude_of_pairs(pairs))
