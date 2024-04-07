def dfs(now, count):
    global arrive
    visited[now] = True
    for i in a[now]:
        if not visited[i]:
            dfs(i, count+1)
    visited[now] = False

    if count > arrive:
        arrive = count

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    count, arrive = 0, 0

    for i in range(m):
        s, e = map(int, input().split())
        a[s].append(e)
        a[e].append(s)

    for i in range(1, n+1):
        dfs(i, 1)

    print(f'#{test_case} {arrive}')