T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    test_case = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    
    while 1:
        num = arr.pop(0)
        num -= cnt
        if num <= 0:
            arr.append(0)
            break
        arr.append(num)
        if cnt == 5:
            cnt = 0
        cnt += 1
    print(f'#{test_case}', *arr)