from collections import deque

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
visited = [[0] * c for i in range(r)]
queue = deque()

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if a[i][j] == "J":
            visited[i][j] = 1
            queue.append((i, j, "J"))
        if a[i][j] == "F":
            visited[i][j] = 1
            queue.appendleft((i, j, "F"))

def bfs(queue):
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and a[nx][ny] == '.':
                    queue.append((nx, ny, z))
                    visited[nx][ny] = visited[x][y] + 1
            else:
                if z == "J":
                    return visited[x][y]

ans = bfs(queue)
print(ans) if ans else print('IMPOSSIBLE')
