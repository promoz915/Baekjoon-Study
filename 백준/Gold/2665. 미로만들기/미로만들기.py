from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(v):
    queue = deque([v])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y]:
                    if not board[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                    else:
                        visited[nx][ny] = visited[x][y]
                    queue.append((nx, ny))


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[1e9] * n for _ in range(n)]
visited[0][0] = 0

bfs((0, 0))
print(visited[n-1][n-1])