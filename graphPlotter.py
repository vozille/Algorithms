import networkx
import matplotlib.pyplot as plot

graph = networkx.Graph()
n,m,k = map(int,raw_input().split())
edges = []
for i in range(m):
    a,b = map(int,raw_input().split())
    edges.append((a,b))
    graph.add_edge(a,b)

pos_graph = networkx.spring_layout(graph)
networkx.draw_networkx_nodes(graph,pos_graph,node_size = 700)
networkx.draw_networkx_edges(graph,pos_graph,edges)
networkx.draw_networkx_labels(graph,pos_graph)

plot.axis('off')
plot.savefig('foo.png')
plot.show()
