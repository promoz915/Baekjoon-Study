import sys
input = sys.stdin.readline

n = int(input())
a = {}
for i in range(n):
    num = int(input())
    if num in a:
        a[num] += 1
    else:
        a[num] = 1

ans = sorted(a.items(), key=lambda x: (-x[1], x[0]))
print(ans[0][0])