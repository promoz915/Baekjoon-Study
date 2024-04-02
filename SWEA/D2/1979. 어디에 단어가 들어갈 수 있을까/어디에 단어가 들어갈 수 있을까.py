T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_zip = list(map(list, zip(*arr)))
    
    def check(arr):
        ans = 0
        for i in range(n):
            cnt = 0
            for j in arr[i]:
                if j == 1:
                    cnt += 1
                else:
                    if cnt == k:
                        ans += 1
                    cnt = 0
            if cnt == k:
                ans += 1
        return ans
    
    ans = check(arr) + check(arr_zip)
    print(f'#{test_case} {ans}')