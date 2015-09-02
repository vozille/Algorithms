graph = [[] for i in range(6)]
n = input()
vertices = set()
for i in range(n):
    a,b = map(int,raw_input().split())
    graph[a].append(b)
    vertices.add(a)
    vertices.add(b)
vertices = list(vertices)
n = len(vertices)
visited = [False]*n

stack = []
def topoSort(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            topoSort(i)
    stack.append(v)

for i in vertices:
    if not visited[i]:
        topoSort(i)

print stack[::-1]
