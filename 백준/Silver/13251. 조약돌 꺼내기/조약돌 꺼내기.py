d = [0] * 51
pro = [0] * 51
m = int(input())
d = list(map(int, input().split()))
t = 0

for i in range(0, m):
    t += d[i]

k = int(input())
ans = 0

for i in range(0, m):
    if d[i] >= k:
        pro[i] = 1
        for j in range(0, k):
            pro[i] = pro[i] * (d[i] - j) / (t - j)
        ans += pro[i]

print(ans)