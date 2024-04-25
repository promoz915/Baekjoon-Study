t = int(input())
ans = []
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]
    cnt1 = 0
    cnt2 = 0

    for d in data:
        if d[::-1] in data and d != d[::-1]:
            cnt1 += m
        elif d[::-1] in data:
            cnt2 = m
    ans.append(f'#{test_case} {cnt1+cnt2}')

for a in ans:
    print(a)