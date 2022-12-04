get_range_set = lambda s: set(range(int(s.split('-')[0]), int(s.split('-')[1])+1))
pairs = [list(map(get_range_set, pair.split(','))) for pair in  open('input').read().strip().split('\n')]

either_subset = lambda pair: pair[0] <= pair[1] or pair[1] <= pair[0]
print('Part 1: ', len(list(filter(either_subset, pairs))))

has_intersection = lambda pair: pair[0].intersection(pair[1])
print('Part 2: ', len(list(filter(has_intersection, pairs))))

