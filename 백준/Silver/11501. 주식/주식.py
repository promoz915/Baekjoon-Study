import sys
input = sys.stdin.readline
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    ans = 0
    max_price = 0

    for i in range(n-1, -1, -1):
        if price[i] >= max_price:
            max_price = price[i]
        else:
            ans += (max_price - price[i])
    print(ans)