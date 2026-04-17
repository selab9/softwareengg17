import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

edges = [(0,10),(0,20),(10,30),(10,40)]
G.add_edges_from(edges)

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(set(graph.neighbors(node)) - set(visited))

    return visited

result = bfs(G,0)
print("BFS Traversal:", result)

nx.draw(G, with_labels=True, node_color='red', node_size=2000)
plt.title("Graph for BFS Traversal")
plt.show()
