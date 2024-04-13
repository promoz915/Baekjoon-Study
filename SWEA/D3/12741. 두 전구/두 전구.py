T = int(input())
ans = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    x = [0] * max(a, b, c, d)
    y = [0] * max(a, b, c, d)
    cnt = 0

    for i in range(a, b):
        x[i] = 1
    for j in range(c, d):
        y[j] = 1
    for a, b in zip(x, y):
        if a and b:
            cnt += 1
    ans.append(f'#{test_case} {cnt}')

print('\n'.join(ans))