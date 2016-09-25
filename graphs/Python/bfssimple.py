"""
Uses Breadth first search to calculate distance of a node from every other node,
assuming the edges have constant/no weight
"""
def BFS(graph, parent, visited, dist):
    visited[parent] = 1
    queue = list()
    queue.append(parent)
    while len(queue) > 0:
        v = queue[0]
        queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                dist[i] = min(dist[v] + 1, dist[i])
                queue.append(i)
    return dist

"""
Represent graph as an adjacency list.
The connected nodes are represented by the edge array,
where [n1, n2] means there's an edge between n1 and n2

N : max limit of number assigned to a node in graph
"""

N = 15
# inf : infinity
inf = float("inf")

graph = [[]for i in range(N)]
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [2, 8], [1, 5], [4, 6], [3, 6], [8, 11]]

# create the graph
for nodes in edges:
    # appending two times represents bidirectional edges
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])

# set distance as infinity (or a very large number)
dist = [inf]*N
# choose your source vertex
src = 1
# set distance of source from itself as zero
dist[src] = 0
# visited must be false for each node since we havent visited any nodes initially
print BFS(graph, src , [0]*N, dist)
