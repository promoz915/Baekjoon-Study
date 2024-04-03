t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))[::-1]
    ans = 0
    max_price = price[0]

    for i in range(n):
        if price[i] > max_price:
            max_price = price[i]
        else:
            ans += (max_price - price[i])
    print(f'#{test_case} {ans}')