def func(x, y):
    i, j = x, y
    row, col = 1, 1
    
    while True:
        x += 1
        if x< n and board[x][y] != 0 and visited[x][y] == False:
            row += 1
        else:
            x -= 1
            break
    
    while True:
        y += 1
        if y < n and board[x][y] != 0 and visited[x][y] == False:
            col += 1
        else:
            y -= 1
            break
            
    for p in range(i, x+1):
        for q in range(j, y+1):
            visited[p][q] = True
    
    return [row, col]


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    ans = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and visited[i][j] == False:
                temp = func(i, j)
                ans.append(temp)
                
    ans = sorted(ans, key=lambda x: ( x[0] * x[1], x[0]))
    print(f'#{test_case} {len(ans)}', end=' ')
    for a in ans:
        print(*a, end=' ')
    print()