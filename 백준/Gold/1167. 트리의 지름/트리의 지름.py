from collections import deque
import sys; input = sys.stdin.readline

n = int(input())                                # 노드 개수
a = [[] for _ in range(n+1)]                    # 그래프 데이터 저장 인접 리스트

for _ in range(n):                              # 노드 수 만큼 반복
    data = list(map(int, input().split()))      # 데이터 입력
    index = 0
    s = data[index]                             # s = 1, 2, 3, ... (데이터 맨 앞 인덱스 역할)
    index += 1
    while True:
        e = data[index]                         # e = destination
        if e == -1:                             # 연결노드 없이 -1이 입력되면 break
            break
        v = data[index + 1]                     # v = distance
        a[s].append((e,v))                      # 리스트에 destination, distance 튜플로 묶어 저장
        index += 2                              # 수가 여러개라면 +2로 다음 노드 거리 확인

distance = [0] * (n+1)                          # 리스트 초기화
visited = [False] * (n+1)                       # 리스트 초기화

def BFS(v):
    queue = deque()
    queue.append(v)                             # 큐에 시작노드 삽입
    visited[v] = True                           # 리스트에 현재 노드 방문 기록
    while queue:
        now_Node = queue.popleft()              # 큐에서 노드 가져오기
        for i in a[now_Node]:                   # 현재의 연결노드
            if not visited[i[0]]:               # 미 방문 노드라면
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1]      # 거리 리스트 업데이트

BFS(1)                                          # 임의의 점 시작점으로 실행
max = 1

for i in range(2, n+1):
    if distance[max] < distance[i]:             # 거리 리스트 값 중 max값으로 시작점 재설정
        max = i

distance = [0] * (n+1)                          # 리스트 초기화
visited = [False] * (n+1)                       # 리스트 초기화
BFS(max)                                        # 새로운 시작점으로 실행
distance.sort()
print(distance[n])                              # 노드 개수 만큼 distance 리스트에서 검색하여 가장 큰 수 출력