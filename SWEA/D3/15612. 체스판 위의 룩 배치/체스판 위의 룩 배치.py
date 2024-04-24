def func(board):
    data = [0] * 8
    for i in range(8):
        if board[i].count('O') != 1:
            return 'no'

        for j in range(8):
            if board[i][j] == 'O' and data[j]:
                return 'no'
            elif board[i][j] == 'O' and not data[j]:
                data[j] = 1
    else:
        return 'yes'

t = int(input())
ans = []
for test_case in range(1, t+1):
    board = [input() for _ in range(8)]
    ans.append(f'#{test_case} {func(board)}')

for a in ans:
    print(a)
