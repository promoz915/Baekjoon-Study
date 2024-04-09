import math

n, k = map(int, input().split())
ans = math.comb(n, k)
ans %= 10007

print(ans)