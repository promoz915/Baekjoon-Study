T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = input()
    a, b = 1, 1
    for i in n:
        if i == 'L':
            b = a + b
        elif i == 'R':
            a = a + b
    print(f'#{test_case} {a} {b}')