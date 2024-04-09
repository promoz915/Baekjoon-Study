T = int(input())
a = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    d, h, m = map(int, input().split())
    ans = 0
    ans += (m-11) + (h-11) * 60 + (d-11) * 24 * 60
    if ans < 0:
        ans = -1
    a.append(ans)
for test_case in range(1, T + 1):
    print(f'#{test_case} {a[test_case-1]}')