from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def func(queue):
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] > distance[x][y] + data[nx][ny]:
                    distance[nx][ny] = distance[x][y] + data[nx][ny]
                    queue.append((nx, ny))
                    
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    distance = [[1e9] * n for _ in range(n)]
    distance[0][0] = data[0][0]
    queue = deque()
    queue.append((0, 0))
    func(queue)
    
    print(f'#{test_case} {distance[n-1][n-1]}')