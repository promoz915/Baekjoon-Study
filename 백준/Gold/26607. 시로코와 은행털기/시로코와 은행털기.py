import sys
input = sys.stdin.readline

n, k, x = map(int, input().split())

powers = []
for _ in range(n):
    nums = input().split()
    powers.append(int(nums[0]))

dp = [[False] * (k+1) for _ in range(x*k+1)]

for p in powers:
    for i in range(x*k, p-1, -1):
        for n_members in range(k-1, 0, -1):
            dp[i][n_members + 1] = dp[i][n_members + 1] or dp[i - p][n_members]
    dp[p][1] = True

optimal_power_1 = (k*x) // 2 + (k*x) % 2
optimal_power_2 = (k*x) // 2

while optimal_power_2 > 0:
    if dp[optimal_power_1][k]:
        break
    if dp[optimal_power_2][k]:
        break
    optimal_power_1 += 1
    optimal_power_2 -= 1

print(str(optimal_power_1 * optimal_power_2))