t = int(input())
ans = []
for test_case in range(1, t+1):
    n = int(input())
    if n % 2:
        ans.append(f'#{test_case} Bob')
    else:
        ans.append(f'#{test_case} Alice')

for a in ans:
    print(a)