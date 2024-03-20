import sys; sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in a[node]:
        if not visited[i]:                          # 방문하지 않은 노드에 대해
            check[i] = (check[node]+1)%2            # 현재 노드와 다른 집합으로 연결 노드 집합 저장
            DFS(i)
        elif check[node] == check[i]:               # 이미 방문한 노드인데, 현재 나의 노드와 같은 집합
            IsEven = False                          # 이분그래프가 아님

for _ in range(n):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    IsEven = True

    for i in range(e):
        start, end = map(int, input().split())
        a[start].append(end)
        a[end].append(start)

    for i in range(1, v+1):                         # 각 노드에서 DFS 실행
        if IsEven:
            DFS(i)
        else:                                       # 결과가 이분그래프가 아니면 반복 종료
            break

    if IsEven:
        print("YES")
    else:
        print("NO")