import sys, re

input = open(sys.argv[1]).read().strip().split('\n')

def naughty(s):
    if 1 not in [len(set((s[i], s[i+2]))) for i in range(len(s)-2)]: return True
    if all([len(s.split(s[i:i+2])) != 3 for i in range(len(s)-1)]): return True

print('Part 2:', list(map(naughty, input)).count(None))
