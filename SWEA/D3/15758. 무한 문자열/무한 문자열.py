t = int(input())
ans = []
for test_case in range(1, t+1):
    s, t = input().split()
    p, q = len(s), len(t)
    if s * q == t * p:
        ans.append(f'#{test_case} yes')
    else:
        ans.append(f'#{test_case} no')

for a in ans:
    print(a)