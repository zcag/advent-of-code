r = [sum(map(int, elf.split('\n'))) for elf in open('input').read().strip().split('\n\n')]
print('part 1:', max(r), '\npart 2:', sum(sorted(r)[-3:]))
