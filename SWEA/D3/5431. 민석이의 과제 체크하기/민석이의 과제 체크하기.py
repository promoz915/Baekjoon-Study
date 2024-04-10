T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    ans = []
    for i in range(1, n+1):
        if i not in data:
            ans.append(i)
    print(f'#{test_case}', *ans)