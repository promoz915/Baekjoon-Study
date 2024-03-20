import sys; input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int,input().split())
a = [[] for _ in range(n+1)]
ans = []
visited = [-1] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()                  # 노드 가져오기
        for i in a[now_Node]:                       # 현재 노드의 연결 노드 중에
            if visited[i] == -1:                    # 미방문 노드가 있다면
                visited[i] = visited[now_Node] + 1  # visited 값 1 증가
                queue.append(i)                     # 큐에 노드 삽입

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)                                  # 입력 데이터 저장

BFS(x)

for i in range(n+1):
    if visited[i] == k:                             # 방문 거리가 k인 노드의 숫자를 정답 리스트에 더하기
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()                                      # 오름차순 정렬 후 출력
    for i in ans:
        print(i)