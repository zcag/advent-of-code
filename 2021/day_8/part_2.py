input = [[[set(sig) for sig in i.strip().split(' ')] for i in l.split('|')] for l in open('input').read().strip().split('\n')]

rule = lambda compare, length, rcompare: next(filter(lambda sig:
                                      (length == None or len(sig) == length)
                                      and (compare == None or d[compare].issubset(sig)
                                      and (rcompare == None or sig.issubset(d[compare]))
                                           ), sigs))
total = 0
for sigs, outs in input:
  d = dict.fromkeys(range(10))
  rules = {1: {'l':2}, 4: {'l':4}, 7: {'l':3}, 8: {'l':7}, 3: {'c':1, 'l':5}, 9: {'c':3}, 0: {'c':1}, 6: {'l':6}, 5: {'rc':6}, 2: {}}
  for i,r in rules.items():
    d[i] = rule(r.get('c', None), r.get('l', None), r.get('rc', None))
    sigs.remove(d[i])
  total += int(''.join([str(list(d.values()).index(out)) for out in outs]))
print(total)
