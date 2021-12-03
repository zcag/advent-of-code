lines = open('input').read().strip()

ratings = []
for sort_key in [lambda x:(-x[0], -counts.index(x)), lambda x:(x[0], counts.index(x))]:
  ls = lines.split('\n')

  for i in range(12):
    counts = [[0, []], [0, []]]

    for num in ls:
      counts[int(num[i])][0] += 1
      counts[int(num[i])][1].append(num)

    ls = sorted(counts, key=sort_key)[0][1]
    if len(ls) == 1:
      ratings.append(int(ls[0], 2))
      continue

print(ratings[0] * ratings[1])
