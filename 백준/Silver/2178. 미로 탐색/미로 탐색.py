from collections import deque
import sys; input = sys.stdin.readline

# 상하좌우 탐색 리스트 선언
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())

# 2차원 배열
a = [[0] * m for _ in range(n)]             # 데이터 저장
visited = [[False] * m for _ in range(n)]   # 방문 기록 저장

for i in range(n):                          # 리스트에 데이터 저장
    numbers = list(input())
    for j in range(m):
        a[i][j] = int(numbers[j])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))                    # 큐에 시작 노드 삽입
    visited[i][j] = True                    # 현재 노드 방문 기록
    while queue:
        now = queue.popleft()               # 큐에서 노드 데이터 가져오기
        for k in range(4):                  # 상하좌우 탐색
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m:   # 좌표 유효성 검사
                if a[x][y] != 0 and not visited [x][y]: # 이동할 수 있는 칸이면서 방문하지 않은 노드
                    visited[x][y] = True                # 방문 기록
                    a[x][y] = a[now[0]][now[1]] + 1     # a 리스트에 depth를 현재 노드의 depth + 1로 업데이트
                    queue.append((x, y))                # 큐에 데이터 삽입

BFS(0, 0)                                   # 시작점 기입
print(a[n-1][m-1])                          # 가야 할 좌표에 따른 결과값 출력