pool = list(map(int, open('input').read().strip().split(',')))


for day in range(80):
  newborn = 0
  for i in range(len(pool)):
    pool[i] -= 1
    if pool[i] == -1:
        pool[i] = 6
        newborn += 1
  pool += [8]*newborn
print(len(pool))
