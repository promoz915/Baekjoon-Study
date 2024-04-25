t = int(input())
ans = []
for test_case in range(1, t+1):
    a, b, c = map(int, input().split())
    x = b - a
    y = c - b
    if x == y:
        ans.append(f'#{test_case} 0.0')
    else:
        ans.append(f'#{test_case} {abs(y-x)/2}')

for a in ans:
    print(a)