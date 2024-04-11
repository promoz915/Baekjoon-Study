T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            data[i] += 1
    p = int(input())
    ans = []
    for _ in range(p):
        c = int(input())
        ans.append(data[c])
    print(f'#{test_case}', *ans)