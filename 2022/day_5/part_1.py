import sys
stacks, ops = open(sys.argv[1]).read().split('\n\n')
stacks = zip(*[row[1::4] for row in stacks.split('\n')[:-1]]) # [(' ', 'N', 'Z'), ('D', 'C', 'M'), (' ', ' ', 'P')]
stacks_1 = [[el for el in stack if el != ' '] for stack in stacks] # [['N', 'Z'], ['D', 'C', 'M'], ['P']]
stacks_2 = [[crate for crate in stack] for stack in stacks_1] # copy for part 2
ops = [map(int, op.split()[1::2]) for op in ops.strip().split('\n')] # [[1, 2, 1], [3, 1, 3]]

for count, stack_src, stack_target in ops:
  stacks_1[stack_target-1][:0] = [stacks_1[stack_src-1].pop(0) for _ in range(count)][::-1]
  stacks_2[stack_target-1][:0] = [stacks_2[stack_src-1].pop(0) for _ in range(count)]

print('Part 1:', ''.join([stack[0] for stack in stacks_1]))
print('Part 2:', ''.join([stack[0] for stack in stacks_2]))
