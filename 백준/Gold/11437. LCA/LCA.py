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
visited = [False] * (n+1)               # 방문 여부 저장 리스트

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1                           # 트리 깊이
    now_size = 1                        # 현재 깊이에서 트리 크기
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

                parent[next] = now_node     # 리스트에 자신의 부모 노드 저장
                depth[next] = level         # 리스트에 현재 깊이 저장
        count += 1
        if count == now_size:               # 현재 깊이의 모든 노드를 방문했다면
            count = 0
            now_size = len(queue)           # 바로 아래 단계 트리 노드 개수 저장
            level += 1

BFS(1)

def lca(a, b):

    # 1번 노드가 depth가 더 작으면 swap
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    # 두 노드의 depth를 동일하게 맞추기
    while depth[a] != depth[b]:
        a = parent[a]

    # 두 노드의 같은 조상이 나올 때 까지 각 노드를 부모 노드로 변경하는 작업 반복
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print((lca(a, b)))