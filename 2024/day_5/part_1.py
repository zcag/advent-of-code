#!/usr/bin/env python3
import sys

rules, updates = [i.split('\n') for i in open(sys.argv[1]).read().strip().split('\n\n')]
updates = [list(map(int, u.split(','))) for u in updates]
rules = [list(map(int, r.split('|'))) for r in rules]

def match(update, rules):
    for rule in rules:
        diff = [u for u in update if u in rule]
        if len(diff) != 2: continue
        if diff != rule: return False
    return True

total = 0
for update in updates:
    if not match(update, rules): continue
    total += update[int(len(update)/2)]

print('Part 1:', total)
