from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for i in range(m):
        s, e  = map(int, input().split())
        a[s].append(e)
        a[e].append(s)
        
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            cnt += 1
            
    print(f'#{test_case} {cnt}')
                    