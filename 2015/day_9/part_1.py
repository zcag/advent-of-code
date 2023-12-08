import sys, re, itertools

input = [re.findall('(\w+) to (\w+) = (\d+)', l)[0] for l in open(sys.argv[1]).read().strip().split('\n')]
distances = {frozenset(i[0:2]): int(i[2])  for i in input}
routes = itertools.permutations(set(sum(map(list, distances.keys()), [])))

score = lambda ls: sum([distances[frozenset((ls[i], ls[i+1]))] for i in range(len(ls)-1)])
scores = [score(route) for route in routes]
print("Part 1:", min(scores), "\nPart 2:", max(scores)) 
