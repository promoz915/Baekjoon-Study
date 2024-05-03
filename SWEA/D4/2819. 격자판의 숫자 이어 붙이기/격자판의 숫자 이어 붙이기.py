dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(idx, x, y, n):
    n += data[x][y]
    
    if idx == 7:
        result.append(n)
        return
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(idx+1, nx, ny, n)


t = int(input())
for test_case in range(1, t+1):
    data = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            dfs(1, i, j, "")
    ans = set(result)
    print(f'#{test_case} {len(ans)}')