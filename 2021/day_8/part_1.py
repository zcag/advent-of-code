input = [[i.strip().split(' ') for i in l.split('|')] for l in open('input').read().strip().split('\n')]
out = [len([c for c in out if len(c) in [2, 4, 3, 7]]) for sig,out in input]
print(sum(out))
