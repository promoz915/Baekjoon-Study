T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = input()
    a = ''
    for i in range(len(data)):
        if data[i] in ['a', 'e', 'i', 'o', 'u']:
            continue
        a += data[i]
    print(f'#{test_case} {a}')