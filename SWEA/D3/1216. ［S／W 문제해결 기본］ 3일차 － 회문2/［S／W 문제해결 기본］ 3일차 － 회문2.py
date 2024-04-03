def pal(n, arr):
    for i in range(n//2):
        if arr[i] != arr[-1-i]:
            return False
    return True

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, 11):
    test_case = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())
    arr_v = list(zip(*arr))
    ans = 1
    flag = False
    
    for n in range(100, 3, -1):
        for i in range(100):
            for j in range(100-n+1):
                if pal(n, arr[i][j:j+n]) or pal(n, arr_v[i][j:j+n]):
                    ans, flag = n, True
                    break
            if flag:
                break
        if flag:
            break
    print(f'#{test_case} {ans}')