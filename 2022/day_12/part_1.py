from queue import PriorityQueue
import string, sys

class Graph:
  def __init__(self, node_count):
    self.node_count = node_count
    self.edges = [[-1 for i in range(node_count)] for j in range(node_count)]
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
        if self.edges[current_vertex][neighbor] == -1 or neighbor in self.visited: continue

        old_cost, new_cost = D[neighbor], D[current_vertex] + self.edges[current_vertex][neighbor]
        if new_cost < old_cost:
          pq.put((new_cost, neighbor))
          D[neighbor] = new_cost
    return D

find = lambda val, grid: [[row.index(val), y] for y, row in enumerate(grid) if val in row]
pos = lambda pos, width: (width * pos[1]) + pos[0]

def neighbors(x, y, x_max, y_max):
  for n_x, n_y in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
    if -1 < n_x < x_max and -1 < n_y < y_max: yield [n_x, n_y]

grid = [list(row) for row in open(sys.argv[1]).read().strip().splitlines()]
width, height = len(grid[0]), len(grid)

start, goal = find('S', grid)[0], find('E', grid)[0]
grid[start[1]][start[0]], grid[goal[1]][goal[0]] = 'a', 'z'

graph = Graph(width*height)
for y in range(height):
  for x in range(width):
    for target in neighbors(x, y, width, height):
      if ord(grid[target[1]][target[0]]) - ord(grid[y][x]) < 2:
        graph.add_edge(pos(target, width), pos([x, y], width), 1)

costs = graph.solve(pos(goal, width))
print('Part 1:', costs[pos(start, width)])
print('Part 2:', min([costs[pos(start, width)] for start in find('a', grid)]))
