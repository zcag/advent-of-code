import sys, re

solve = lambda x: len(x)-(len(re.findall(r"(?:\\x[0-9a-fA-F]{2})|(?:\\?.)", x))-2)
output = sum(map(solve, open(sys.argv[1]).read().strip().split('\n')))
print("Part 1: ", output)
