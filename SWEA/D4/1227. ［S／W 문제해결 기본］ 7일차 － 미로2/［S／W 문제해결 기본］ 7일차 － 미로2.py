from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def func(a, b):
    global visited
    queue = deque()
    queue.append((a, b))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] in [0, 3] and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                if data[nx][ny] == 3:
                    return True
                
            
for _ in range(1, 11):
    test_case = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    x, y = 1, 1
    visited = []
    
    if func(x, y):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')