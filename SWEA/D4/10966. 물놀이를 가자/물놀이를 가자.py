from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    visited = [[-1] * m for _ in range(n)]
    
    queue = deque()
    for i in range(n):
        place = input()
        for j in range(m):
            if place[j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0
                
    bfs()
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += visited[i][j]
            
    print(f'#{test_case} {ans}')