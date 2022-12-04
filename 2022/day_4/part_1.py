input = open('input').read().strip().split('\n')

# Implementation with sets:
get_range_set = lambda s: set(range(int(s.split('-')[0]), int(s.split('-')[1])+1))
pairs = [list(map(get_range_set, pair.split(','))) for pair in input]

contains = lambda a, b: a <= b or b <= a
overlaps = lambda a, b: len(a.intersection(b)) != 0

print('Part 1: ', sum(map(contains, *zip(*pairs))))
print('Part 2: ', sum(map(overlaps, *zip(*pairs))))

# Implementation with boolean logic:
pairs = [[list(map(int, sector.split('-'))) for sector in pair.split(',')] for pair in input]

contains = lambda a, b: (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])
overlaps = lambda a, b: (b[0] <= a[0] <= b[1]) or (a[0] <= b[0] <= a[1])

print('Part 1: ', sum(map(contains, *zip(*pairs))))
print('Part 2: ', sum(map(overlaps, *zip(*pairs))))
