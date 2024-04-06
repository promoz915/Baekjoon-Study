from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ans = 0

def bfs(x, y):
    a[x][y] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = 1
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                q.append([nx, ny])
                a[nx][ny] = 0
                count += 1
    return count

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt)
print(ans)