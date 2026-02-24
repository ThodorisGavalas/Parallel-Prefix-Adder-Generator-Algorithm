import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edge('bit3L0','bit3L1')
G.add_edge('bit2L0','bit3L1')
G.add_edge('bit1L0','bit1L1')
G.add_edge('bit0L0','bit1L1')
G.add_edge('bit3L1','bit3L2')
G.add_edge('bit1L1','bit3L2')
G.add_edge('bit2L0','bit2L2')
G.add_edge('bit1L1','bit2L2')
nodes= {'bit0L0':(-0,0),'bit1L0':(-1,0),'bit2L0':(-2,0),'bit3L0':(-3,0),'bit3L1':(-3,-1),'bit1L1':(-1,-1),'bit3L2':(-3,-2),'bit2L2':(-2,-2)}
first_nodes = list(nodes.keys())[:4] # Get the first 4 nodes
numeric_labels = {node: str(i) for i, node in enumerate(first_nodes)} ## Create numeric labels (0, 1, 2, 3...) for the first 4 nodes
nx.draw(G,pos=nodes) # Draw the graph with all nodes
nx.draw_networkx_labels(G, pos=nodes, labels=numeric_labels, font_color='white') # Add labels with numeric names for the first 4 nodes and white color
plt.show()