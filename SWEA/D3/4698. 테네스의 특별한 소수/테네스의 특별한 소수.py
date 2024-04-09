prime = [2]
MOD = 1000001
visited = [0] * MOD

for i in range(3, MOD, 2):
    if visited[i] == 0:
        prime.append(i)
        for j in range(i, MOD, i):
            if j % i == 0:
                visited[j] = 1
                
T = int(input())

for test_case in range(1, T + 1):
    d, a, b = map(int, input().split())
    ans = 0
    for p in prime:
        if a <= p <= b:
            if str(d) in str(p):
                ans += 1
        elif p > b:
            break
    print(f'#{test_case} {ans}')