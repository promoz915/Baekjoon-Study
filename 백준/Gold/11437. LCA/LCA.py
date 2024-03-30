import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(0, n-1):                 # 노드가 n개 이므로 연결선은 n-1개
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n+1)                     # 노드 깊이 리스트
parent = [0] * (n+1)                    # 노드 조상 리스트
result = {}

def BFS(node):
    queue = deque([node])
    depth[node] = 1                     # 최초 노드에 depth 1 초기화

    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not depth[next]:                     # 미방문 노드일 때
                parent[next] = now_node             # 리스트에 자신의 부모 노드 저장
                depth[next] = depth[now_node] + 1   # 리스트에 현재 깊이 저장
                queue.append(next)                  # 리스트에 자식 노드 저장

BFS(1)

def lca(s, e):

    if s > e:
        s, e = e, s

    a, b = s, e                 # 함수 내에서 사용할 변수에 복사

    # 메모이제이션, 이미 정답 쌍에 저장된 값일 시 바로 반환
    if (a, b) in result:
        return result[(a, b)]

    # 두 노드의 depth를 동일하게 맞추기
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 두 노드의 같은 조상이 나올 때 까지 각 노드를 부모 노드로 변경하는 작업 반복
    while a != b:
        a = parent[a]
        b = parent[b]
    
    # 메모이제이션을 위한 정답 저장
    result[(s, e)] = a
    return a

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print((lca(a, b)))