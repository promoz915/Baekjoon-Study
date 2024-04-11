T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]
    w = [int(input()) for _ in range(m)]
    data = [int(input()) for _ in range(m*2)]

    park = [0] * n
    wait = []
    price = 0

    for i in data:
        if i > 0:
            if 0 not in park:
                wait.append(i)
            else:
                idx = park.index(0)
                park[idx] = i
                price += r[idx] * w[i-1]
        else:
            idx = park.index(abs(i))
            if wait:
                j = wait.pop(0)
                park[idx] = j
                price += r[idx] * w[j-1]
            else:
                park[idx] = 0
    print(f'#{test_case} {price}')