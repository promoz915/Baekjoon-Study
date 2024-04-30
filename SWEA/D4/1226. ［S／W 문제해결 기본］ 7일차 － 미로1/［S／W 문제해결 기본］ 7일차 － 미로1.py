from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(1, 11):
    test_case = int(input())
    data = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    queue = deque()
    queue.append((1, 1))
    visited[1][1] = 1
    ans = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < 16 and 0 <= ny < 16:
                if data[nx][ny] == '3':
                    ans = 1
                    break
                if data[nx][ny] == '0' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    
    print(f'#{test_case} {ans}')