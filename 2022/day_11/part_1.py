import math, sys

def monkey_bussiness(round=20, worry_manager_v2=False):
  monkeys = {}
  for text in open(sys.argv[1]).read().strip().split('\n\n'):
    parts = [bit for bits in text.split(':') for bit in bits.split('\n')]
    monkeys[int(parts[0].split()[1])] = {
        'items': list(map(int, parts[3].split(','))),
        'op': parts[5].split('=')[-1],
        'test': int(parts[7].split()[-1]),
        'out': {True: int(parts[9].split()[-1]), False: int(parts[11].split()[-1])},
        'inspected': 0
        }

  modulo = math.prod([monkey['test'] for monkey in monkeys.values()])

  for _ in range(round):
    for monkey in monkeys.values():
      for old in monkey['items'][::-1]:
        if worry_manager_v2: new = eval(monkey['op'])%modulo
        else: new = int(eval(monkey['op'])/3)

        target = monkey['out'][new%monkey['test'] == 0]
        monkeys[target]['items'].append(new)
        monkey['items'].remove(old)
        monkey['inspected'] += 1

  return math.prod(sorted([monkey['inspected'] for monkey in monkeys.values()])[-2:])

print('Part 1:', monkey_bussiness(20))
print('Part 2:', monkey_bussiness(10000, True))

