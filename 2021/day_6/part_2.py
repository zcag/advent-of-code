ls = [0]*9
for n in open('input').read().split(','): ls[int(n)] += 1

for _ in range(256):
 ls.append(ls.pop(0))
 ls[6] += ls[8]

print(sum(ls))
