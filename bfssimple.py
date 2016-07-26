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
