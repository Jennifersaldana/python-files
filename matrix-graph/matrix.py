import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('TkAgg')  # or 'Agg', 'Qt5Agg', etc.
#import matplotlib
#matplotlib.use('TkAgg')  # Ensure this line is uncommented if you face backend issues.


# Create the adjacency matrix using NumPy
# graph = np.array([
#     [0, 3, 0, 2],
#     [3, 0, 1, 1],
#     [0, 1, 1, 2],
#     [2, 1, 2, 0]
# ])

graph = np.array([
    [1, 2, 0, 1],
    [2, 0, 3, 0],
    [0, 3, 1, 1],
    [1, 0, 1, 0]
])

# Accessing elements of the matrix
print(graph[0, 1]) 


# Create a graph object
G = nx.from_numpy_array(graph)

# Draw the graph with node labels and edge weights
pos = nx.spring_layout(G)  # or use any layout you prefer
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): graph[i, j] for i, j in G.edges if graph[i, j] > 0})

plt.title("Graph Representation of Adjacency Matrix")
plt.show()
plt.savefig("graph.png")
