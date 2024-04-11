import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()
mn = int(2e9)

e = 0
for s in range(n):
    while e < n and data[e] - data[s] < m:
        e += 1
    if e == n:
        break
    mn = min(mn, data[e] - data[s])
print(mn)