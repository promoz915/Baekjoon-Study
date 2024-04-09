T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(int(input()))

    arr = []
    cnt = 0

    for i in range(1, len(data)):
        if data[i] in arr:
            continue

        temp = data[i] - 1
        for j in range(data[i], data[-1]+1, temp):
            arr.append(j)
        cnt += 1

    print(f'#{test_case} {cnt}')