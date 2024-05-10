import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = 0

left, right = 0, int(1e5) * 20 + 1
while left <= right:
    mid = (left+right)//2
    group, temp = 0, 0
    for d in data:
        temp += d
        if temp >= mid:
            group += 1
            temp = 0
    if group >= k:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)           