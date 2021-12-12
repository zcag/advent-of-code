import collections, json
nodes = collections.defaultdict(list)
for l in open('testinput').read().strip().split('\n'): nodes[l.split('-')[0]].append(l.split('-')[1])

done = False
d = json.loads(json.dumps(nodes))
paths = []
while not done:
 print(d)
 paths = d['start']
 done = True
