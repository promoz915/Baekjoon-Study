t = int(input())
result = []

for test_case in range(1, t+1):
    n = int(input())
    ans = [0] * 5
    check = [2, 3, 5, 7, 11]

    for i in range(4, -1, -1):
        while n % check[i] == 0:
            ans[i] += 1
            n //= check[i]
    result.append(f'#{test_case} {" ".join(map(str, ans))}')

for r in result:
    print(r)