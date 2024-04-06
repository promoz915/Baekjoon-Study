from collections import deque

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                a[nx][ny] = a[x][y] + 1
                queue.append([nx, ny])
bfs()
for i in a:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)