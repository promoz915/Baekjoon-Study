T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(data[i]):
                ans += data[i][j]
    print(f'#{test_case} {ans}')