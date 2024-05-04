dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def func(start):
    global n
    
    cnt = 0
    stack = [start]
    
    while stack:
        x, y = stack.pop()
        cnt += 1
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < n:
                if data[x][y] + 1 == data[nx][ny]:
                    stack.append((nx, ny))
    return cnt


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = [float('inf'), 0]
    
    for i in range(n):
        for j in range(n):
            cnt = func((i, j))
            
            if cnt > ans[1]:
                ans[1] = cnt
                ans[0] = data[i][j]
                
            elif cnt == ans[1]:
                if ans[0] > data[i][j]:
                    ans[0] = data[i][j]
                    
    print(f'#{test_case} {ans[0]} {ans[1]}')