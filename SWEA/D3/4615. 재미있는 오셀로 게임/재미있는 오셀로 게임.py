dir_board = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    temp = n//2
    board[temp][temp] = 2
    board[temp-1][temp-1] = 2
    board[temp][temp-1] = 1
    board[temp-1][temp] = 1

    for i in range(m):
        x, y, c = map(int, input().split())
        x, y = x-1, y-1

        data = []
        for i in range(8):
            dx, dy = dir_board[i]
            nx = x + dx
            ny = y + dy
            while True:
                if not(0 <= nx < n and 0 <= ny < n):
                    data = []
                    break
                if board[nx][ny] == 0:
                    data = []
                    break
                if board[nx][ny] == c:
                    break
                else:
                    data.append((nx, ny))
                nx = nx + dx
                ny = ny + dy

            for x_val, y_val in data:
                if c == 1:
                    board[x_val][y_val] = 1
                elif c == 2:
                    board[x_val][y_val] = 2
        board[x][y] = c
    w_val, b_val = 0, 0
    for i in range(n):
        w_val += board[i].count(2)
        b_val += board[i].count(1)

    print(f'#{test_case} {b_val} {w_val}')