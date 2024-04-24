t = int(input())
ans = []
for test_case in range(1, t+1):
    n = int(input())
    ans.append(f'#{test_case} {n*n}')

for a in ans:
    print(a)