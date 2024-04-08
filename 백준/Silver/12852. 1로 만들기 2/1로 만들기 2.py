import sys
input = sys.stdin.readline

n = int(input())
a = [0] * (n+1)
arr = []
for i in range(2, n+1):
    a[i] = a[i-1] + 1
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1)
print(a[n])

now = n
arr.append(n)
temp = a[n]-1
for i in range(n, 0, -1):
    if a[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        arr.append(i)
        temp -= 1
print(*arr)