src = [i for i in range(105)]

# union find
def find(x):
    while src[x] != x:
        src[x] = src[src[x]]
        x = src[x]
    return x

def union(a,b):
    x = find(a)
    y = find(b)
    src[x] = src[y]

def kruskal(graph):
    graph = sorted(graph)
    minCost = 0
    for i in range(len(graph)):
        u = graph[i][1]
        v = graph[i][2]

        if find(u) != find(v):
            minCost += graph[i][0]
            union(u,v)
    return minCost

graph = [[5,1,2],[7,2,3],[1,3,4],[2,1,3]]
print kruskal(graph)
