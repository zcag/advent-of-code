import sys, re, itertools

input = open(sys.argv[1]).read().strip()
say = lambda x: ''.join([f"{len(s)}{s[0]}" for s, _ in re.findall(r"((\d)\2*)", x)])

for i in range(50):
    if i == 40: print('Part 1: ', len(input))
    input = say(input)
print("Part 2: ", len(input))
