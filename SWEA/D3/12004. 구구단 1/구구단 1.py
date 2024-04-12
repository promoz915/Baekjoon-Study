T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    flag = False
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            flag = True
    if flag:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')