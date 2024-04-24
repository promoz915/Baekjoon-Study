t = int(input())
ans = []
for test_case in range(1, t+1):
    n = int(input())
    i, j = n*9, n*8
    ans.append(f'#{test_case} {i} {j}')

for a in ans:
    print(a)