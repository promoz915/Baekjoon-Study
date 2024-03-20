import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]

def BFS(v):
    queue = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1

    while queue:
        now_Node = queue.popleft()
        for i in a[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

for _ in range(m):
    s, e = map(int, input().split())
    a[e].append(s)

ans = [0] * (n+1)
for i in range(1, n+1):
    ans[i] = BFS(i)

maxVal = max(ans)

for i in range(1, n+1):
    if maxVal == ans[i]:                        # ans 리스트에서 maxVal과 같은 값을 가진 index 출력
        print(i, end=' ')