import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [1] * (n+1)
data = []
for i in range(m):
    a, b = map(int, input().split())
    data.append((a, b))
data.sort()
for a, b in data:
    if A[b] <= A[a]:
        A[b] = A[a] + 1
print(*A[1:])