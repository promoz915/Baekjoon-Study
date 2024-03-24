import sys
from queue import PriorityQueue
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
distance = [sys.maxsize] * (v+1)        # 거리 저장 리스트
visited = [False] * (v+1)               # 방문 여부 저장 리스트
myList = [[] for _ in range(v+1)]       # 에지 데이터 저장 인접 리스트
q = PriorityQueue()                     # 다익스트라를 위한 우선순위 큐

for _ in range(e):
    a, b, c = map(int, input().split())
    myList[a].append((b, c))            # 인접 리스트에 에지 정보 저장

q.put((0, k))                           # 출발 노드는 q에 넣고 시작
distance[k] = 0                         # 거리 리스트에 출발 노드의 값을 0으로 설정

while q.qsize() > 0:                    # 큐가 빌 때 까지
    current = q.get()                   # 우선순위 큐에서 현재 노드 가져오기
    c_v = current[1]
    if visited[c_v]:                    # 현재 선택된 노드를 방문한 적이 있는지 확인
        continue
    visited[c_v] = True                 # 현재 노드를 방문 노드로 업데이트
    for tmp in myList[c_v]:
        next = tmp[0]                   # 도착값
        value = tmp[1]                  # 가중치

        if distance[next] > distance[c_v] + value:  # 현재 선택 노드 최단 거리 + 비용 < 연결 노드의 최단 거리
            distance[next] = distance[c_v] + value  # 연결 노드 최단 거리 업데이트
            q.put((distance[next], next))           # 우선순위 큐에 연결 노드 추가(가중치, 목표 노드 순)
                                                
for i in range(1, v+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")