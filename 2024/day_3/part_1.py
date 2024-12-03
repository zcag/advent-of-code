#!/usr/bin/env python3
import sys, re
from math import prod

input = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', open(sys.argv[1]).read())
print('Part 1:', sum(prod(map(int,o)) for o in input))
