import sys, re, functools

parse = lambda l,r: [r, l.split()]
ops = dict([parse(*l.split(' -> ')) for l in open(sys.argv[1]).read().strip().split('\n')])

@functools.cache
def solve(wire):
    if wire not in ops: return int(wire)
    value = ops[wire]
    if type(value) == int : return value
    if type(value) == list and len(value) == 1:
        if value[0].isnumeric(): return int(value[0])
        else: return solve(value[0])

    l, op, r = value if len(value) == 3 else [None, *value]
    l, r = solve(l) if l else None, solve(r)

    match op:
        case 'NOT': return solve(r) ^ 0xFFFF
        case 'AND': return solve(l) & solve(r)
        case 'OR': return solve(l) | solve(r)
        case 'LSHIFT': return solve(l) << solve(r)
        case 'RSHIFT':  return solve(l) >> solve(r)

print('Part 1: ', solve('a'))
ops['b'] = solve('a')
solve.cache_clear()
print('Part 2: ', solve('a'))
