n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if a[i] not in s:
            s.append(a[i])
            dfs()
            s.pop()
dfs()
