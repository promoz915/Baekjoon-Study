from collections import deque
import sys; input = sys.stdin.readline

n, m = map(int ,input().split())
a = [[] for i in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):                      # 인접 리스트 데이터 저장
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1                    # 진입 차수 데이터 저장

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:                # 진입 차수 값이 0인 노드를 큐에 삽입
        queue.append(i)

while queue:                            # 위상 정렬 수행
    now = queue.popleft()               # 큐에서 데이터 가져오기
    print(now, end=' ')
    for next in a[now]:                 # 현재 노드에서 갈 수 있는 노드의 개수
        indegree[next] -= 1             # 타깃 노드 진입 차수 리스트값 1 감소
        if indegree[next] == 0:         # 타깃 노드의 진입 차수가 0이면
            queue.append(next)          # 큐에 타깃 노드 추가