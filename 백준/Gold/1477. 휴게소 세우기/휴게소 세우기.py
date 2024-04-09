n, m, l = map(int, input().split())
data = [0] + list(map(int, input().split())) + [l]
data.sort()

s, e = 1, l-1
ans = 0
while s <= e:
    cnt = 0
    mid = (s+e) // 2
    for i in range(1, len(data)):
        if data[i] - data[i-1] > mid:
            cnt += (data[i] - data[i-1] - 1) // mid
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid
print(ans)