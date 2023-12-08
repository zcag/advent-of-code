import sys, re, collections, math

input = [(h,int(b)) for h,b in [l.split() for l in open(sys.argv[1]).read().strip().split('\n')]]
vals = ''.join(map(str,range(2, 10))) + 'TJQKA'

def score(h, joker=False):
    if joker:
        rep = [('J' + vals.replace('J', '')).index(c) for c in h]
        counts = sorted(collections.Counter(h.replace('J', '')).values(), reverse=True) + [0]
        counts[0] = min(5, counts[0]+h.count('J'))
    else:
        counts = list(collections.Counter(h).values())
        rep = [vals.index(c) for c in h]
    
    if 5 in counts: hp = 10 # Five of a kind
    elif 4 in counts: hp = 9 # Four of a kind
    elif 3 in counts and 2 in counts: hp = 8 # Full house
    elif 3 in counts: hp = 7 # Three of a kind
    elif counts.count(2) == 2: hp = 6 # Two pair
    elif 2 in counts: hp = 5 # Pair
    else: hp = 4 # High

    return [hp] + rep

for part in range(2):
    bids = list(zip(*sorted(input, key=lambda x: score(x[0], joker=part))))[1]
    print(f"Part {part+1}: ", sum(map(math.prod, enumerate(bids, 1))))
