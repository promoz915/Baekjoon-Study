import sys; input = sys.stdin.readline

n, m, k = map(int, input().split())
d= [[0 for j in range(202)] for i in range(202)]
MOD = 1000000000

for i in range(201):
    for j in range(i+1):
        if j == 0 or j == i:
            d[i][j] = 1
        else:
            d[i][j] = d[i-1][j] + d[i-1][j-1]
            if d[i][j] > MOD:
                d[i][j] = MOD + 1

if d[n+m][m] < k:                   # n+m 개에서 m을 뽑는 경우의 수가 k보다 적을 때
    print(-1)
else:
    while not (n == 0 and m == 0):  # 모든 문자를 사용할 때 까지
        
        # d[n-1+m][m] : 남아 있는 문자들로 만들 수 있는 모든 경우의 수
        if d[n-1+m][m] >= k:        # a를 선택해도 남은 경우의 수가 k보다 큰 경우
            print("a", end="")
            n -= 1
        else:
            print("z", end='')
            k -= d[n-1+m][m]
            m -= 1