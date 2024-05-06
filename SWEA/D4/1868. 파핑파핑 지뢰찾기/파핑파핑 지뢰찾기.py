from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def if_click(x, y):
    global cnt
    next_target = []
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == '.':
                next_target.append((nx, ny))
            elif board[nx][ny] == '*':
                break
    else:
        if next_target:
            board[x][y] = 'o'
            cnt += 1
            spread(next_target)
            
            
def spread(lst):
    queue = deque(lst)
    while queue:
        x, y = queue.popleft()
        board[x][y] = 'o'
        next_next_target = []
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == '.':
                    next_next_target.append((nx, ny))
                elif board[nx][ny] == '*':
                    break
        else:
            spread(next_next_target)
            
        
def no_spread():
    global cnt
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                cnt += 1


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                if_click(i, j)
    
    no_spread()
    print(f'#{test_case} {cnt}')