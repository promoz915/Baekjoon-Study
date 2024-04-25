# import sys
# sys.stdin = open("sample_input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cutting):
    global visited, ans
    ans = max(ans, visited[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:    # 부지
            continue

        if data[x][y] > data[nx][ny]:                               # 낮은 높이의 등산로로 가는 길이 있으면
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cutting)
            visited[nx][ny] = 0

        elif cutting and data[nx][ny] - k < data[x][y]:             # cutting 횟수가 있고, 최대 공사 후 가는 길이 있으면
            temp = data[nx][ny]
            data[nx][ny] = data[x][y] - 1
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cutting-1)
            visited[nx][ny] = 0
            data[nx][ny] = temp

t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]      # 지도 정보 받기
    visited = [[0] * n for _ in range(n)]                           # 접근 유무
    ans = 0             # 최종 등산로 길이
    h = 0               # 높이

    # 최대 높이 계산
    for i in range(n):
        for j in range(n):
            if data[i][j] > h:
                h = data[i][j]

    # dfs 수행
    for i in range(n):
        for j in range(n):
            if data[i][j] == h:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print(f'#{test_case} {ans}')
