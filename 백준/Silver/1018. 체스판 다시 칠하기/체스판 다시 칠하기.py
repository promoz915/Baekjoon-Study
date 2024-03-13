n, m = map(int, input().split())

board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        w_start = 0
        b_start = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        w_start += 1
                    if board[a][b] != 'W':
                        b_start += 1
                else:
                    if board[a][b] != 'W':
                        w_start += 1
                    if board[a][b] != 'B':
                        b_start += 1

        result.append(w_start)
        result.append(b_start)

print(min(result))