from copy import deepcopy


def per(data, d):
    for i in range(len(data)):
        if d == 1:
            yield [data[i]]
        else:
            for j in per(data[:i] + data[i+1:], d-1):
                yield [data[i]] + j
                
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
rcs = [list(map(int, input().split())) for _ in range(k)]

ans = 1e9

for p in per(rcs, k):
    cpa = deepcopy(a)
    for r, c, s in p:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):
            tmp = cpa[r-n][c+n]
            cpa[r-n][c-n+1:c+n+1] = cpa[r-n][c-n:c+n]
            for row in range(r-n, r+n):
                cpa[row][c-n] = cpa[row+1][c-n]
            cpa[r+n][c-n:c+n] = cpa[r+n][c-n+1:c+n+1]
            for row in range(r+n, r-n, -1):
                cpa[row][c+n] = cpa[row-1][c+n]
            cpa[r-n+1][c+n] = tmp
    for row in cpa:
        ans = min(ans, sum(row))

print(ans)