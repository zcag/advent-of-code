pool = list(map(int, open('input').read().strip().split(',')))

ls = [0]*9

for i in pool: ls[i] += 1

for day in range(256):
 popped = ls.pop(0)
 ls.append(popped)
 ls[6] += popped

print(sum(ls))
