import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
ans = []
for i in range(n):
    ans.append(a[i]*(i+1))
print(max(ans))