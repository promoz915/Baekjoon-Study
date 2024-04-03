import sys
input = sys.stdin.readline

# dp[N][L][R] : N개 수열을 수행했고, 왼쪽이 L 오른쪽이 R에 있을 때 최소 누적
# 충분히 큰 수로 초기화
dp = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
# 한 발을 이동할 때 드는 힘을 미리 저장하기(mp[1][2] -> 1에서 2로 이동할 때 드는 힘)
mp = [[0, 2, 2, 2, 2],
      [2, 1, 3, 4, 3],
      [2, 3, 1, 3, 4],
      [2, 4, 3, 1, 3],
      [2, 3, 4, 3, 1]]


s = 1               # 수열 진행값

dp[0][0][0] = 0     # 처음에는 아무 힘이 들지 않은 상태로 시작

arr = list(map(int, input().split()))
idx = 0

while arr[idx] != 0:
    n = arr[idx]    # 이동해야 할 입력 값
    # 오른쪽 다리를 이동해 현재 다리 위치로 만들 수 있는 경우의 수
    for i in range(5):
        if n == i:  # 두 발이 같은 자리에 있는 경우
            continue
        for j in range(5):  # j : 이전 위치
            dp[s][i][n] = min(dp[s-1][i][j] + mp[j][n], dp[s][i][n])
            
    # 왼쪽 다리를 이동해 현재 다리 위치로 만들 수 있는 경우의 수
    for j in range(5):
        if n == j:  # 두 발이 같은 자리에 있는 경우
            continue
        for i in range(5):  # j : 이전 위치
            dp[s][n][j] = min(dp[s-1][i][j] + mp[i][n], dp[s][n][j])
    s += 1
    idx += 1

s -= 1  # 마지막 이동 횟수로 index 조정
result = sys.maxsize

for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])

print(result)