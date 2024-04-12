T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    d, l, n = map(int, input().split())
    damage = int(d*n + d*l*n*(n-1)/200)
    print(f'#{test_case} {damage}')