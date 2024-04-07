n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
visited = [False] * n
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    temp = 0
    for i in range(start, n):
        if not visited[i] and temp != a[i]:
            visited[i] = True
            s.append(a[i])
            temp = a[i]
            dfs(i+1)
            visited[i] = False
            s.pop()
dfs(0)
