#!/usr/bin/env python3
import sys
from functools import cmp_to_key

rules, updates = [i.split('\n') for i in open(sys.argv[1]).read().strip().split('\n\n')]
updates = [list(map(int, u.split(','))) for u in updates]
rules = [list(map(int, r.split('|'))) for r in rules]
rule_cmp = lambda x,y: -1 if [x,y] in rules else 1

totals = {True: 0, False: 0}
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(rule_cmp))
    totals[sorted_update == update] += sorted_update[int(len(sorted_update)/2)]

print('Part 1:', totals[True], '\nPart 2:', totals[False])

