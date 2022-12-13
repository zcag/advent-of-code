import sys

input = open(sys.argv[1]).read().strip().split('\n')
pairs = [[list(map(int, sector.split('-'))) for sector in pair.split(',')] for pair in input]

contains = lambda a, b: (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])
overlaps = lambda a, b: (b[0] <= a[0] <= b[1]) or (a[0] <= b[0] <= a[1])

print('Part 1:', sum(map(contains, *zip(*pairs))))
print('Part 2:', sum(map(overlaps, *zip(*pairs))))
