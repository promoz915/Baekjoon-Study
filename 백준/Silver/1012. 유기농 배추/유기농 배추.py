import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(a, b):
    if a <= -1 or a >= n or b <= -1 or b >= m:      # 경계 확인
        return False

    if arr[a][b] == 1:
        arr[a][b] = 0                               # 해당 위치 방문 표시
        for i in range(4):                          # 상하좌우 좌표 재귀표시
            DFS(a + dx[i], b + dy[i])
        return True
    return False

ans = []
for _ in range(t):
    m, n, k = list(map(int, input().split()))       # m : 가로, n : 세로, k : 지렁이 위치
    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1                               # 입력 위치 뒤바꿔야 함

    cnt = 0
    for i in range(n):
        for j in range(m):
            if DFS(i, j):
                cnt += 1
    print(cnt)
