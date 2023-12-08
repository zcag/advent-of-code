import sys, re

solve = lambda v,f,r,t: (int(t/(f+r))*v*f) + min(f, t-int(t/(f+r))*(f+r))*v
input = [list(map(int, re.findall('\d+', l))) for l in open(sys.argv[1]).read().strip().split('\n')]

points = [0 for _ in input]
for t in range(1, 2503):
    results = [(solve(*deer, t), deer) for deer in input]
    winning_dist = max(results, key=lambda r: r[0])[0]
    winning_indexes = [i for i in range(len(results)) if results[i][0] == winning_dist]
    for i in winning_indexes: points[i] += 1

print('Part 2: ', max(points))
