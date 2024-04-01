T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num = set()
    cnt = 0
    while len(num) != 10:
        cnt += 1
        num.update(set(str(n*cnt)))
    print(f'#{test_case} {n*cnt}')