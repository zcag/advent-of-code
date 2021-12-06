with open('input') as f: lines = f.read().split('\n')[:-1]
out = 0
for i in range(1, len(lines)-1):
    n1 = int(lines[i])
    n0 = int(lines[i-1])
    out += 1 if n1>n0 else 0
print(out)
