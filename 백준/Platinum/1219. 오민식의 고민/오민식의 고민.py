import sys
input = sys.stdin.readline

n, s, e, m = map(int, input().split())
edges = []
distance = [-sys.maxsize] * n

for _ in range(m):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

distance[s] = cityMoney[s]                      # 거리 리스트에 출발노드 cityMoney[출발노드]로 초기화

# 양수 사이클이 전파되도록 충분히 큰 수로 반복
for i in range(n + 101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:     # 출발 노드가 미 방문 노드면 skip
            continue
        elif distance[start] == sys.maxsize:    # 출발 노드가 양수 사이클에 연결되어 있으며
            distance[end] = sys.maxsize         # 종료 노드를 양수 사이클에 연결된 노드로 업데이트

        # 더 많은 수입을 얻는 경로가 새로 발견되는 경우 값 업데이트
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= n-1:
                distance[end] = sys.maxsize     # 종료 노드를 양수 사이클 연결 노드로 업데이트

if distance[e] == -sys.maxsize:
    print("gg")
elif distance[e] == sys.maxsize:
    print("Gee")
else:
    print(distance[e])