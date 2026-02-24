def printNetworkX (seq,n):
    bitspan = list(range(n))
    levels = [0 for i in range(n)]
    nodes=[]
    edges=[]
    for i in range(len(seq)):
        
        nodeposition = seq[i][0] # bit position of the new node and the more significant node connecting to the new node
        overlap = seq[i][1]
        LSBposition  = bitspan[seq[i][0]] - 1+overlap # bit position of the less significant node connecting to the new node
        MSBlevel = levels[nodeposition] # level of the more important node
        LSBlevel = levels[LSBposition] # level of the less important node
        
        levels[seq[i][0]] = max(MSBlevel,LSBlevel) + 1 # the level of the new node is at a level one higher than the highest of these 2 levels
        
        nodelevel = levels[seq[i][0]] # the level of the new node
        
        bitspan[seq[i][0]] = bitspan[bitspan[seq[i][0]] - 1 +overlap]
        
        nodes.append([nodeposition,nodelevel])
        edges.append([[nodeposition,MSBlevel],[nodeposition,nodelevel],[LSBposition,LSBlevel]])
    edgescode = [f"G.add_edge('bit{edge[0][0]}L{edge[0][1]}','bit{edge[1][0]}L{edge[1][1]}'){chr(10)}G.add_edge('bit{edge[2][0]}L{edge[2][1]}','bit{edge[1][0]}L{edge[1][1]}')" for edge in edges]
    firstnodes = [f"'bit{i}L0':(-{i},0)" for i in range(n)]
    operators  = [f"'bit{node[0]}L{node[1]}':(-{node[0]},-{node[1]})" for node in nodes]
    coordinates = firstnodes + operators
    NetworkXcode= f"""import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
{chr(10).join(edgescode)}
nodes= {{{','.join(coordinates)}}}
first_nodes = list(nodes.keys())[:{n}] # Get the first {n} nodes
numeric_labels = {{node: str(i) for i, node in enumerate(first_nodes)}} ## Create numeric labels (0, 1, 2, 3...) for the first {n} nodes
nx.draw(G,pos=nodes) # Draw the graph with all nodes
nx.draw_networkx_labels(G, pos=nodes, labels=numeric_labels, font_color='white') # Add labels with numeric names for the first {n} nodes and white color
plt.show()"""
    print(NetworkXcode)
    
printNetworkX([[3,0],[1,0],[3,0],[2,0]],4)
