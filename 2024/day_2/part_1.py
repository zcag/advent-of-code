#!/usr/bin/env python3
import sys

input = [list(map(int,l.split(" "))) for l in open(sys.argv[1]).read().strip().split('\n')]
ordered = lambda l: sorted(l) == l or sorted(l)[::-1] == l
safe_dist = lambda l: all([0 < abs(l[i-1] - l[i]) < 4 for i in range(1, len(l))])
print('Part 1:', sum([ordered(l) and safe_dist(l) for l in input]))
