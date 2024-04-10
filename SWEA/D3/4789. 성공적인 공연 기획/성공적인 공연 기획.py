T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(str(input()))
    ans = 0
    acc = 0
    
    for i in range(len(data)):
        if data[i] != 0:
            if acc >= i:
                acc += int(data[i])
            else:
                ans += i - acc
                acc = i + int(data[i])
    print(f'#{test_case} {ans}')