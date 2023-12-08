import sys

class Graph:
  def __init__(self, node_count):
    self.node_count = node_count
    self.edges = [[None for i in range(node_count)] for j in range(node_count)]
    self.visited = []

  def add_edge(self, u, v, weight): self.edges[u][v] = weight

  def solve(self, start_vertex):
    D = {v:float('inf') for v in range(self.node_count)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
      (dist, current_vertex) = pq.get()
      self.visited.append(current_vertex)

      for neighbor in range(self.node_count):
        if self.edges[current_vertex][neighbor] == None or neighbor in self.visited: continue

        old_cost, new_cost = D[neighbor], D[current_vertex] + self.edges[current_vertex][neighbor]
        if new_cost < old_cost:
          pq.put((new_cost, neighbor))
          D[neighbor] = new_cost
    return D


def shortcuts():

lines = shortcuts(list(map(str.split, open(sys.argv[1]).read().strip().split('\n'))))


pressures = {l[1]: int(l[4].split('=')[1][:-1]) for l in lines}
paths = {l[1]: ''.join(l[9:]).split(',') for l in lines}
tunnels = [l[1] for l in lines]

g = Graph(len(tunnels))
for tunnel in tunnels:
  for path in paths[tunnel]:
    g.add_edge(tunnels.index(tunnel), tunnels.index(path), -pressures[path])

d = g.solve('AA')

print(minute)
print(pressure)


print(pressures)
print(paths)



