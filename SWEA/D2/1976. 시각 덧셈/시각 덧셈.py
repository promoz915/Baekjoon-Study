T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    ans_h = h1 + h2; ans_m = m1 + m2
    if ans_h > 12:
        ans_h -= 12
    if ans_m > 60:
        ans_h += 1
        ans_m -= 60
    print(f'#{test_case} {ans_h} {ans_m}')