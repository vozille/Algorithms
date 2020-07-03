def main(grid: list, sr: int, sc: int, newColor: int):
    node_queue = collections.deque([])
    node_queue.append(list([sr, sc]))
    source = grid[sr][sc]
    grid[sr][sc] = newColor

    dx = [1, -1, 0, 0]
    dy = [0 ,0 ,1 ,-1]

    def bfs():

        while len(node_queue):
            for _ in range(len(node_queue)):
                curr = node_queue.popleft()
                for i in range(4):
                    x = curr[0] + dx[i]
                    y = curr[1] + dy[i]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == source:
                        grid[x][y] = newColor
                        node_queue.append(list([x, y]))

    bfs()
    return grid


if __name__ == '__main__':
    print(main([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
