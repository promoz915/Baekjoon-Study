from collections import deque
import sys; input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]
indegree = [0] * (n+1)                          # 진입 차수 리스트
selfBuild = [0] * (n+1)                         # 자기 자신을 짓는 데 걸리는 시간 저장 리스트

for i in range(1, n+1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])               # 건물을 짓는데 걸리는 시간
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:                       # -1 이 입력되면 종료
            break
        a[preTemp].append(i)
        indegree[i] += 1                        # 진입 차수 데이터 저장

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:                        # 진입 차수 리스트의 값이 0이면
        queue.append(i)                         # 건물(노드)을 큐에 삽입

result = [0] * (n+1)

# 위상 정렬 수행
while queue:
    now = queue.popleft()
    for next in a[now]:                         # 현재 노드에서 갈 수 있는 노드 탐색
        indegree[next] -= 1                     # 타깃 노드 진입 차수 리스트 1 감소

        # 결과 노드 업데이트 = max(현재 저장된 값, 현재 출발 노드 + 비용)
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:                 # 타깃 노드의 진입 차수가 0이면
            queue.append(next)                  # 우선순위 큐에 타깃 노드 추가

for i in range(1, n+1):
    print(result[i] + selfBuild[i])