import sys, re

input = open(sys.argv[1]).read().strip().split('\n')

def naughty(s):
    if any([c in s for c in 'ab cd pq xy'.split()]): return True
    if len(re.findall('[aeiou]', s)) < 3: return True
    if 1 not in [len(set(s[i:i+2])) for i in range(len(s)-1)]: return True

print('Part 1:', list(map(naughty, input)).count(None))
