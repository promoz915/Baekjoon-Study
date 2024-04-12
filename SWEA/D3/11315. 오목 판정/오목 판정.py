dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

def func():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'o':
                for k in range(4):
                    nx = i
                    ny = j
                    cnt = 0
                    
                    while 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[k]
                        ny += dy[k]
                        
                    if cnt == 5:
                        return 'YES'
    return 'NO'

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = [input() for _ in range(n)]
    print(f'#{test_case} {func()}')