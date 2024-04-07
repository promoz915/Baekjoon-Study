def dfs(i, count):
    global ans
    if count == k:
        ans += 1
        return
    if i == n:
        return
    dfs(i+1, count + data[i])
    dfs(i+1, count)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    ans = 0
    dfs(0,0)
    print(f'#{test_case} {ans}')