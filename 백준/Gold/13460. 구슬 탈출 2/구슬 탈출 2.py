from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = []
queue = deque()

rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            rx, ry = i, j
        if data[i][j] == 'B':
            bx, by = i, j

queue.append([rx, ry, bx, by, 1])
visited.append([rx, ry, bx, by])

def go(x, y, i, j):
    cnt = 0
    while data[x+i][y+j] != '#' and data[x][y] != 'O':
        x += i
        y += j
        cnt += 1
    return x, y, cnt

def bfs():
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        if cnt > 10:
            print(-1)
            return

        for i in range(4):
            nrx, nry, nr_cnt = go(rx, ry, dx[i], dy[i])
            nbx, nby, nb_cnt = go(bx, by, dx[i], dy[i])

            if data[nbx][nby] == 'O':
                continue

            if data[nrx][nry] == 'O':
                print(cnt)
                return

            if nrx == nbx and nry == nby:
                if nr_cnt > nb_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]

                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if [nrx, nry, nbx, nby] not in visited:
                visited.append([nrx, nry, nbx, nby])
                queue.append([nrx, nry, nbx, nby, cnt + 1])
    print(-1)

bfs()
