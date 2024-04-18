import sys
input = sys.stdin.readline

def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if data[i][j] != 0 and data[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != -1:
                        arr[nx][ny] += data[i][j] // 5
                        tmp += data[i][j] // 5
                data[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            data[i][j] += arr[i][j]

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    direct = 0
    before = 0
    x, y = up, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        data[x][y], before = before, data[x][y]
        x = nx
        y = ny

def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direct = 0
    before = 0
    x, y = down, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        data[x][y], before = before, data[x][y]
        x = nx
        y = ny

r, c, t = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1

for i in range(r):
    if data[i][0] == -1:
        up = i
        down = i+1
        break

for _ in range(t):
    spread()
    air_up()
    air_down()

ans = 0
for i in range(r):
    for j in range(c):
        if data[i][j] > 0:
            ans += data[i][j]

print(ans)