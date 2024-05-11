import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    if x == out1 and y == out2:
        return True
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '@':
            board[nx][ny] = '.'
            if dfs(nx, ny):
                return True
            board[nx][ny] = '@'
    return False

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

hole = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                hole.append((i, j))
            board[i][j] = '@'
            
ent1, ent2 = hole[0]
out1, out2 = hole[1]

ans = dfs(ent1, ent2)
board[ent1][ent2] = '.'

for b in board:
    print(''.join(b))