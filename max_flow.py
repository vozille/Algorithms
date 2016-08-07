# max flow problem
# ford fulkerson algorithm
"""
    in max flow algo, we implement a traversal algo like bfs/dfs
    then we pick a path from source to sink
    then if we find a augmenting path which stays in range of the limit of the capacity of edges
    we add that path
    we do dfs/bfs till we cannot find any more augmenting paths
    the parent array just stores the path

    subtract flow from sink to source
    add flow from source to sink

    TIP : for weighted graphs, a list of maps is a much better option

"""

class Graph:
    def __init__(self, n):
        self._graph = [[] for i in range(n + 1)]
        self._revGraph = [[] for i in range(n + 1)]
        self.__entries = [0 for i in range(n + 1)]
        self.__vertices = set()

    def add_uni_edge(self, a, b, w=1):
        self.__vertices.add(a)
        self.__vertices.add(b)
        if w == 1:
            self._graph[a].append(b)
            self.__entries[b] += 1
            self.__entries[a] -= 1
            self._revGraph[b].append(a)
        else:
            self._graph[a].append([b, w])
            self._revGraph[b].append([a, w])

    def add_bi_edge(self, a, b, w=1):
        self.__vertices.add(a)
        self.__vertices.add(b)
        if w == 1:
            self._graph[a].append(b)
            self._graph[b].append(a)
        else:
            self._graph[a].append([b, w])
            self._graph[b].append([a, w])

    def get_graph(self):
        return self._graph

    def get_rev_graph(self):
        return self._revGraph

    def get_vertices(self):
        return list(self.__vertices)

    def all_balanced_vertex(self):
        for i in self.get_vertices():
            if self.__entries[i] > 0:
                return False
        return True


def dfs(graph, src, sink , parent):
    visited = [0]*len(graph)
    visited[src] = 1
    parent[src] = -1
    queue = [src]
    while len(queue) > 0:
        v = queue[0]
        queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    return visited[sink] == 1


def ford_fulkerson(graph, source, sink):
    residual_graph = deepcopy(graph)
    parent = [0]*len(residual_graph)
    flow = int(10**10)
    max_flow = 0
    while dfs(residual_graph, source, sink, parent):
        u = sink
        while u != source:
            flow = min(flow, residual_graph[parent[u][u]])
            u = parent[u]
        u = sink
        # update new flow values
        while u != source:
            residual_graph[parent[u]][u] -= source
            residual_graph[u][parent[u]] += source
            u = parent[u]
        max_flow += flow
    return max_flow
