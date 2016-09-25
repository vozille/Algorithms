"""
cycle in directed graph
"""
maxm = 104
visited = [False]*maxm
recStack = [False]*maxm

vertices = set()
graph = [[] for i in range(maxm)]
for i in range(input()):
    a,b = map(int,raw_input().split())
    vertices.add(a)
    vertices.add(b)
    graph[a].append(b)

def dfs(graph,curr,recursion_stack):
    visited[curr] = True
    recStack[curr] = True
    for i in graph[curr]:

        if not visited[i]:
            if dfs(graph,i,recStack):
                return True

        elif recStack[i]:
            return True
    recStack[curr] = False
    return False
vertices = list(vertices)

for i in vertices:
    if not visited[i]:
        print dfs(graph,i,recStack)


"""
cycle in undirected graph
"""

maxm = 300004
visited = [False]*maxm

vertices = set()
graph = [[] for i in range(maxm)]
for i in range(input()):
    a,b = map(int,raw_input().split())
    vertices.add(a)
    vertices.add(b)
    graph[a].append(b)
    graph[b].append(a)

res = []
def dfs(graph,curr,parent):
    visited[curr] = True
    for i in graph[curr]:
        if not visited[i]:
            if dfs(graph,i,curr):
                return True
        elif i != parent:
            return True
    return False

vertices = list(vertices)

for i in vertices:
    res = []
    visited = [False]*maxm
    print dfs(graph,i,-1)
