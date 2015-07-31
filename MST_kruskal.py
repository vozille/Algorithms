src = [i for i in range(10**5)]

# path compression
def root(x):
    while src[x] != x:
        src[x] = src[src[x]]
        x = src[x]
    return x

def unionFind(a,b):
    x = root(a)
    y = root(b)
    src[x] = src[y]

def kruskal(graph):
    graph = sorted(graph)
    minCost = 0
    for i in range(len(graph)):
        u = graph[i][1]
        v = graph[i][2]

        if root(u) != root(v):
            minCost += graph[i][0]
            unionFind(u,v)
    return minCost

graph = [[5,1,2],[7,2,3],[1,3,4],[2,1,3]]
print kruskal(graph)
