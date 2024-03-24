import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
w = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * k for _ in range(n+1)]      # 2차원 값으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    w[a].append((b, c))

pq = [(0, 1)]                                           # 우선순위 큐에 시작노드 저장(가중치, 목표 노드 순서)
distance[1][0] = 0                                      # 시작 도시 최단 거리 저장

while pq:
    cost, node = heapq.heappop(pq)                      # (거리, 노드) 데이터 가져오기
    for nNode, nCost in w[node]:                        # 현재 노드에서 연결된 에지 탐색
        sCost = cost + nCost                            # 새로운 총 거리 = 현재 노드의 거리 + 에지 가중치

        if distance[nNode][k-1] > sCost:                # 새로운 노드의 k번째 최단거리 > 새로운 총 거리
            distance[nNode][k-1] = sCost                # 업데이트
            distance[nNode].sort()                      # 거리 순으로 정렬
            heapq.heappush(pq, [sCost, nNode])   # 우선순위 큐에 새로운 데이터 추가 (거리, 노드)

for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])