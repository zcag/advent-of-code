#!/usr/bin/env python3
import sys

input = zip(*[map(int, l.split("   ")) for l in open(sys.argv[1]).read().strip().split('\n')])
output = sum([abs(l-r) for l,r in zip(*[sorted(l) for l in input])])
print('Part 1:', output)
