import sys, re

input, output = open(sys.argv[1]).read().strip().split('\n'), 0
for l in input:
    matches = re.findall('\d', l)
    output += int(matches[0]+matches[-1])
print('Part 1', output)
