n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
ans = []
def func(v):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1
    for i in range(v, n):
        ans.append(a[i])
        func(i+1)
        ans.pop()
func(0)
print(cnt)