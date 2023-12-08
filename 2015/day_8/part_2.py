import sys, re

solve = lambda x: len(re.findall(r"[\\\"]", x)) + 2
output = sum(map(solve, open(sys.argv[1]).read().strip().split('\n')))
print("Part 2: ", output)
