import sys; input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

left = [0] * n
left[0] = a[0]
result = left[0]

for i in range(1, n):
    left[i] = max(a[i], left[i-1] + a[i])
    result = max(result, left[i])

right = [0] * n
right[n-1] = a[n-1]

for i in range(n-2, -1, -1):
    right[i] = max(a[i], right[i+1] +a[i])

for i in range(1, n-1):
    temp = left[i-1] + right[i+1]
    result = max(result, temp)

print(result)