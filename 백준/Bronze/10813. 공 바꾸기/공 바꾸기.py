n, m = map(int, input().split())
b = list(range(n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    b[i], b[j] = b[j], b[i]

print(*b[1:])