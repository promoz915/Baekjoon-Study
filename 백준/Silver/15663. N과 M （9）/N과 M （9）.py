n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
visited = [False] * n
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    temp = 0
    for i in range(n):
        if not visited[i] and temp != a[i]:
            visited[i] = True
            s.append(a[i])
            temp = a[i]
            dfs()
            visited[i] = False
            s.pop()
dfs()
