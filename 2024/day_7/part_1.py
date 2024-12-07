#!/usr/bin/env python3
import sys, operator
from itertools import product
from functools import reduce

input = [l.split(': ') for l in open(sys.argv[1]).read().strip().split('\n')]
input = [(int(i[0]), list(map(int, i[1].split(' ')))) for i in input]

OPERATORS = [operator.mul, operator.add]
op_combos = lambda count: [list(ops) for ops in product(OPERATORS, repeat=count-1)]

calc = lambda args, ops: reduce(lambda x, y: ops.pop(0)(x, y), args)
valid = lambda res, args: any([res == calc(args[::], ops) for ops in op_combos(len(args))])

print('Part 1:', sum([res for res, args in input if valid(res, args)]))
