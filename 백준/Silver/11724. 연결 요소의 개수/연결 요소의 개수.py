import sys; input = sys.stdin.readline; sys.setrecursionlimit(10000)
n, m = map(int, input().split())
a = [[] for _ in range(n+1)]            # n+1 반복하여 a에 리스트 추가
visited = [False] * (n+1)               # 방문 기록 리스트 초기화

def DFS(v):
    visited[v] = True                   # visited 리스트에 현재 노드(v) 방문 기록
    for i in a[v]:                      # 현재 노드의 연결 노드 중
        if not visited[i]:              # 방문하지 않은 노드로 DFS 실행
            DFS(i)                      # 재귀함수 이용

for _ in range(m):                      # 에지 범위 만큼(5)
    s, e = map(int, input().split())    # 데이터 입력
    a[s].append(e)                      # 방향 없는 그래프이므로 서로 append 입력
    a[e].append(s)

count = 0

for i in range(1, n+1):                 # 노드의 수(1~6) 반복
    if not visited[i]:                  # 방문 하지 않은 노드가 있다면
        count += 1                      # count + 1
        DFS(i)                          # DFS 실행

print(count)