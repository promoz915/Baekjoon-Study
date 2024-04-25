t = int(input())
ans = []
for test_case in range(1, t+1):
    a, b = map(int, input().split())
    if a == b:
        gcd = a
    else:
        gcd = 1
    ans.append(f'#{test_case} {gcd}')

for a in ans:
    print(a)