with open('input') as f: foods = f.read().split('\n')[:-1]
elves = [0]
for food in foods:
  if food == '': elves.append(0)
  else: elves[-1] += int(food)
print('part 1: ', max(elves))
print('part 2: ', sum(sorted(elves)[-3:]))
