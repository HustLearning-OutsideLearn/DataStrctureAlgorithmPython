class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

class graph_vertex:
  def __init__(self, name, x, y):
    self.name = name
    self.position = (x, y)
  
  def __lt__(self, other):
    return self.name < other.name
