n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

s = 1
k = max(lst)

while s <= k:
    mid = (s+k)//2
    lan = 0
    for i in lst:
        lan += i//mid
    if lan >= m:
        s = mid + 1
    else:
        k = mid - 1

print(k)