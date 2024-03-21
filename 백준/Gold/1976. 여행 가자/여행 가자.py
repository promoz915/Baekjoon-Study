import sys; input = sys.stdin.readline

n = int(input())
m = int(input())
dosi = [[0 for j in range(n+1)] for i in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, n+1):                         # 도시 연결 데이터 저장
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)         # index 1부터 시작이기 때문에 0번째에 0 데이터 삽입 필요

route = list(map(int, input().split()))         # 여행 도시 정보 저장
route.insert(0, 0)               # index 1부터 시작이기 때문에 0번째에 0 데이터 삽입 필요

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):                         # 인접 행렬에서 도시가 연결되어 있으면 union 실행
    for j in range(1, n+1):
        if dosi[i][j] == 1:
            union(i, j)

index = find(route[1])
isConnect = True

for i in range(2, len(route)):                  # 여행 계획 도시들이 1개의 대표 도시로 연결돼 있는지 확인
    if index != find(route[i]):                 # route에 포함되는 노드들의 대표 노드가 모두 동일한지 확인
        isConnect = False                       # 다르다면 isConnect에 False 삽입
        break

if isConnect:
    print("YES")
else:
    print("NO")