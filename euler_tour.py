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


def dfs(graph, src, visited):
    visited[src] = 1
    for i in graph[src]:
        if not visited[i]:
            dfs(graph, i, visited)
            # do stuff here
    return visited

# for ssc, check if all nodes can be visited via dfs in normal as well as reversed graph from same source
# for euler, check if all entries values are zero along with ssc

# test

mygraph = Graph(5)
mygraph.add_uni_edge(1, 2)
mygraph.add_uni_edge(2, 3)
mygraph.add_uni_edge(3, 1)

visited = [0]*(6)
x = dfs(mygraph.get_rev_graph(), mygraph.get_vertices()[0], visited)
print x
print mygraph.all_balanced_vertex()
