import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
mn = int(1e9)
tot = data[0]
e = 0

for s in range(n):
    while e < n and tot < m:
        e += 1
        if e != n:
            tot += data[e]
    if e == n:
        break
    mn = min(mn, e - s + 1)
    tot -= data[s]

if mn == int(1e9):
    mn = 0
print(mn)