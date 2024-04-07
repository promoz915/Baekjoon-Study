n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    temp = 0
    for i in range(start, n):
        if temp != a[i]:
            s.append(a[i])
            temp = a[i]
            dfs(i)
            s.pop()
dfs(0)
