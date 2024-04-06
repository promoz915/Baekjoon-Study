from collections import deque

m, n, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
ans = 0

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and a[nx][ny][nz] == 0:
                a[nx][ny][nz] = a[x][y][z] + 1
                queue.append([nx, ny, nz])

for o in range(h):
    for p in range(n):
        for q in range(m):
            if a[o][p][q] == 1:
                queue.append([o, p, q])

bfs()
for i in a:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        ans = max(ans, max(j))
print(ans - 1)