T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = list(input())
    ans = 0
    arr = list(0 for i in range(len(n)))
    for i in range(len(arr)):
        if int(n[i]) != arr[i]:
            for j in range(i, len(arr)):
                arr[j] = int(n[i])
            ans += 1
        else:
            continue
    print(f'#{test_case} {ans}')