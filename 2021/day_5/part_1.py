input = open('input').read().strip().split('\n')

all_cords = []
for line in input:
  cords = [[int(n) for n in i.split(',')] for i in line.split(' -> ')]
  if cords[0][0] != cords[1][0] and cords[0][1] != cords[1][1]: continue

  cords.sort(key=lambda x:(x[0], x[1]))
  diffi = 1 if cords[0][0] == cords[1][0] else 0
  consti = 1 if diffi == 0 else 0

  for i in range(cords[0][diffi], cords[1][diffi]):
    cord = [0, 0]
    cord[diffi] = i
    cord[consti] = cords[0][consti]
    cords += [cord]
  all_cords += cords[1:]

d = { (i[0], i[1]):all_cords.count(i) for i in all_cords }
print(len([v for v in d.values() if v > 1]))
