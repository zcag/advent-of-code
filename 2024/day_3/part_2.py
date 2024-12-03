#!/usr/bin/env python3
import sys, re
from math import prod

pattern, do, res = r'(do(?:n\'t)?\(\))|(?:mul\((\d{1,3}),(\d{1,3})\))', True, 0
for op in re.findall(pattern, open(sys.argv[1]).read()):
    if len(op[0]): do = "don't" not in op[0]
    elif do: res += prod(map(int, op[1:]))
print('Part 2:', res)
