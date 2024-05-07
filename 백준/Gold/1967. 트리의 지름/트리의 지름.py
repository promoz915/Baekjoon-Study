from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, d = map(int, input().split())
    a[p].append((c, d))
    a[c].append((p, d))

distance = [0] * (n+1)
visited = [False] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

bfs(1)
max = 1

for i in range(2, n+1):
    if distance[max] < distance[i]:
        max = i

distance = [0] * (n+1)
visited = [False] * (n+1)
bfs(max)
distance.sort()
print(distance[n])