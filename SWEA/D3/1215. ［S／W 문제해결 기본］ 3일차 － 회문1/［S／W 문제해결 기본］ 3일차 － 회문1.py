def pal(arr):
    ans = 0
    for word in arr:
        for i in range(8-n+1):
            target = word[i:i+n]
            if target == target[::-1]:
                ans += 1
    return ans

for test_case in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    ans = pal(arr)
    arr = list(zip(*arr))
    ans += pal(arr)
    print(f'#{test_case} {ans}')