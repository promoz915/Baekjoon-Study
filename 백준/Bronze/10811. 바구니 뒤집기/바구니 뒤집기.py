n, m = map(int, input().split())
b = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    t = b[i-1:j]
    t.reverse()
    b[i-1:j] = t

for i in range(n):
    print(b[i], end=" ")