
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    data = list(map(int, input().split()))
    sorted_data = sorted(data, reverse=True)
    i = 0
    result = []

    while n < len(sorted_data):
        if sorted_data[i] * 0.75 in sorted_data:
            idx = sorted_data.index(sorted_data[i] * 0.75)
            temp = sorted_data.pop(idx)
            result.append(temp)
            i += 1
        else:
            result.append(data[i])
            sorted_data.pop(i)
    re_data = sorted(result)
    print(f'#{test_case}', *re_data)
