bags = open('input').read().strip().split('\n')

chars = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
common_score = lambda l: chars.index(set.intersection(*map(set, l)).pop())

bag_compartments = [(bag[:int(len(bag)/2)], bag[int(len(bag)/2):]) for bag in bags]
print('Part 1:', sum(map(common_score, bag_compartments)))

elf_groups = [bags[i:i+3] for i in range(0, len(bags), 3)]
print('Part 2:', sum(map(common_score, elf_groups)))
