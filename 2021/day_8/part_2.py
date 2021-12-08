input = [[[set(sig) for sig in i.strip().split(' ')] for i in l.split('|')] for l in open('input').read().strip().split('\n')]

out = [len([c for c in out if len(c) in [2, 4, 3, 7]]) for sig,out in input]

total = 0
for sigs, outs in input:
  d = {0: None, 1:None, 2: None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None,  9:None}
  for num, size in {1: 2, 4: 4, 7: 3, 8:7}.items():
    d[num] = next(filter(lambda x:len(x)==size, sigs))
  d[3] = next(filter(lambda sig:len(sig) == 5 and d[1].issubset(sig), sigs))
  d[6] = next(filter(lambda sig:len(sig) == 6 and not d[1].issubset(sig), sigs))
  d[9] = next(filter(lambda sig:len(sig) == 6 and d[3].issubset(sig), sigs))
  sigs = [sig for sig in sigs if sig not in d.values()]
  d[0] = next(filter(lambda sig:len(sig) == 6, sigs))
  d[2] = next(filter(lambda sig:len(d[6].difference(sig)) == 2, sigs))
  sigs = [sig for sig in sigs if sig not in d.values()]
  d[5] = sigs[0]
  decode_map = list(d.values())
  total += int(''.join([str(decode_map.index(out)) for out in outs]))
print(total)
