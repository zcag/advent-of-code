import sys, re

d = dict(zip('one two three four five six seven eight nine'.split(' '), range(1,10)))
patterns = ['|'.join(d) + '|\d', '.*(?=('+('|'.join(d)) + '|\d))']

res = []
for line in open(sys.argv[1]).read().strip().split('\n'):
    combined = re.search(patterns[0], line).group() + re.findall(patterns[1], line)[-1]
    for k,v in d.items(): combined = re.sub(k, str(v), combined)
    res.append(int(combined))

print('Part 2', sum(res))
