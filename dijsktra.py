from Queue import *
for testCases in range(input()):
    maxm = 3005
    graph = [[] for i in range(maxm)]
    dist = [10**12]*maxm
    visited = [False]*maxm

    v,e = map(int,raw_input().split())
    vertices = set()
    for i in range(e):
        a,b,w = map(int,raw_input().split())
        vertices.add(a)
        vertices.add(b)
        graph[a].append([b,w])
        graph[b].append([a,w])
    n = input()
    vertices = sorted(list(vertices))
    print vertices
    pq = PriorityQueue()

    dist[n] = 0
    pq.put((0,n))
    while not pq.empty():
        b = pq.get()[1]
        if not visited[b]:
            for i in graph[b]:
                a = i[0]
                w = i[1]
                if not visited[a] and dist[b] + w < dist[a]:
                    dist[a] = dist[b] + w
                    pq.put((dist[a],a))
            visited[b] = True

    for i in vertices:
        if dist[i] == 0:
            continue
        if dist[i] == 10**12:
            print '-1',
        else:
            print dist[i],
    print
