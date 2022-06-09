import matplotlib.pyplot as plt
import networkx as nx
G=nx.read_adjlist('adj.txt', create_using=nx.DiGraph())
pos=nx.shell_layout(G)
nx.draw_networkx_nodes(G,pos, node_color='#00D0FF', alpha=0.8)
nx.draw_networkx_edges(G,pos, width = 1.0,alpha=0.5)
labels=nx.draw_networkx_labels(G,pos,font_size=14)
plt.axis('on')
plt.show()