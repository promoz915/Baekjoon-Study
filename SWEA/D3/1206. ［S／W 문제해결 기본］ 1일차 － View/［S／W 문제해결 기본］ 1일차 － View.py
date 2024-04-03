for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2):
        left = max(arr[i-1], arr[i-2])
        right = max(arr[i+1], arr[i+2])
        max_val = max(left, right)
        if arr[i] > max_val:
            ans += arr[i] - max_val

    print(f'#{test_case} {ans}')