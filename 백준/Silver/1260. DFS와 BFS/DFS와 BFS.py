from collections import deque
import sys; input = sys.stdin.readline

n, m, start = map(int, input().split())
a = [[] for _ in range(n+1)]                # 그래프 데이터 저장 인접 리스트

for _ in range(m):                          # 양방항 에지이므로 양쪽에 에지 더하기
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n+1):                        # 작은 수인 노드부터 접근하기 위해 정렬
    a[i].sort()

def DFS(v):
    print(v, end=' ')                       # 현재 노드 출력하기
    visited[v] = True                       # 방문 알림
    for i in a[v]:                          # 현재 노드의 연결 노드 중
        if not visited[i]:                  # 방문하지 않는 노드에 대해
            DFS(i)                          # 재귀함수 적용

visited = [False] * (n + 1)                 # 리스트 초기화
DFS(start)

def BFS(v):
    queue = deque()
    queue.append(v)                         # 큐에 시작 노드 삽입
    visited[v] = True
    while queue:
        now_Node = queue.popleft()          # 큐에서 노드 데이터 가져오기
        print(now_Node, end=' ')            # 가져온 노드 출력
        for i in a[now_Node]:               # 현재 노드의 연결 노드 중
            if not visited[i]:              # 방문하지 않은 노드에 대해
                visited[i] = True           # 방문 리스트에 기록
                queue.append(i)             # 큐에 삽입

print()                                     # 한줄 띄기
visited = [False] * (n + 1)                 # 리스트 초기화
BFS(start)