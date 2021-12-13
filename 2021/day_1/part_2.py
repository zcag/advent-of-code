with open('input') as f: lines = list(map(int, f.read().strip().split('\n')))

out = 0
last = 999999999
for i in range(0, len(lines)-2):
    current = sum(lines[i:i+3])
    out += 1 if current>last else 0
    last = current

print(out)
