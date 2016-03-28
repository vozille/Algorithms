import math
# log(V) time complexity, V*log(V) space complexity
class LowestCommonAncestor:
    def __init__(self, graph, size, root):
        """
        :param graph: the graph as adjagency list
        :param size: the number of vertices in graph
        :param root: the root vertex
        :return: void
        """
        self.graph = graph
        self.visited = [0 for i in range(size + 1)]
        self.prev = [-1 for i in range(size + 1)]
        self.depth = [10**10 for i in range(size + 1)]
        self.BFS(root)
        k = int(math.log(size + 1 ,2)) + 1
        self.partition = [[-1 for i in range(k)] for i in range(size + 1)]
        self.preprocess()

    def BFS(self, src):
        self.visited[src] = 1
        self.depth[src] = 0
        self.prev[src] = src
        queue = []
        queue.append(src)
        while len(queue) > 0:
            v = queue[0]
            queue.pop(0)
            for i in self.graph[v]:
                if not self.visited[i]:
                    self.prev[i] = v
                    self.depth[i] = self.depth[v] + 1
                    queue.append(i)
                    self.visited[i] = 1

    def preprocess(self):
        """
        preprocesses the partition array
        :return:
        """
        for i in range(len(self.partition)):
            self.partition[i][0] = self.prev[i]
        j = 1
        while 2**j < len(self.partition):
            for i in range(len(self.partition)):
                if self.partition[i][j - 1] != -1:
                    self.partition[i][j] = self.partition[self.partition[i][j - 1]][j - 1]
            j += 1

    def LCA(self, u, v):
        """
        Finds lowest common ancestor
        :param u: vertex u
        :param v: vertex v
        :return: integer distance between u and v
        """
        if self.depth[u] < self.depth[v]:
            u,v = v,u
        log = int(math.log(self.depth[u],2))
        for i in range(log, -1, -1):
            if self.depth[u] - 2**i >= self.depth[v]:
                u = self.partition[u][i]
        if u == v:
            return u
        for i in range(log, -1, -1):
            if self.partition[u][i] != -1 and self.partition[u][i] != self.partition[v][i]:
                u = self.partition[u][i]
                v = self.partition[v][i]
        return self.prev[u]
