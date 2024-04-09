T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    temp = ''
    while True:
        temp += ''.join(map(str, input().split()))
        if len(temp) == n: break
    
    ans = 0
    cnt = 0
    while True:
        if str(cnt) not in temp:
            ans = cnt
            break
        cnt += 1
    print(f'#{test_case} {ans}')