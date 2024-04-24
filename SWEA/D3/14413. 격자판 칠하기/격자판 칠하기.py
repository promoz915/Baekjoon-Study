T = int(input())
ans = []
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    board = [0, 0, 0, 0]
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == '#':
                if (i+j) % 2 == 0:
                    board[0] += 1
                else:
                    board[1] += 1
            elif data[i][j] == '.':
                if (i+j) % 2 == 0:
                    board[2] += 1
                else:
                    board[3] += 1
    if (board[0] and board[1]) or (board[2] and board[3]) or (board[0] and board[2]) or (board[1] and board[3]):
        ans.append(f'#{test_case} impossible')
    else:
        ans.append(f'#{test_case} possible')
        
for a in ans:
    print(a)