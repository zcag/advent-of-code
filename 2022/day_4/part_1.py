# Implementation with sets:
get_range_set = lambda s: set(range(int(s.split('-')[0]), int(s.split('-')[1])+1))
pairs = [list(map(get_range_set, pair.split(','))) for pair in  open('input').read().strip().split('\n')]

contains = lambda a, b: a <= b or b <= a
overlaps = lambda a, b: len(a.intersection(b)) != 0

print('Part 1: ', sum(map(contains, *zip(*pairs))))
print('Part 2: ', sum(map(overlaps, *zip(*pairs))))

