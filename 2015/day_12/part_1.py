import sys, re, json

print('Part 1: ', sum(map(int, re.findall('-?\d+', open(sys.argv[1]).read().strip()))))

def sumj(j):
    if isinstance(j, list): return sum(map(sumj, j))
    if isinstance(j, dict): return 0 if 'red' in j.values() else sumj(list(j.values()))
    return j if type(j) == int else 0

print('Part 2: ', sumj(json.load(open(sys.argv[1]))))
