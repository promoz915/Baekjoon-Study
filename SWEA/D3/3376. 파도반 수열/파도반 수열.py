T = int(input())
data = [1, 1, 1]
for i in range(3, 101):
    data.append(data[i-2]+data[i-3])
for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {data[n-1]}')