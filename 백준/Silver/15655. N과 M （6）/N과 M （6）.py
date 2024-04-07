n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n):
        if a[i] not in s:
            s.append(a[i])
            dfs(i+1)
            s.pop()
dfs(0)
