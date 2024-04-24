t = int(input())
result = []
for test_case in range(1, t+1):
    s = input()
    ans = 0
    ans += s.count('()')
    ans += s.count('(|')
    ans += s.count('|)')
    result.append(f'#{test_case} {ans}')

for r in result:
    print(r)