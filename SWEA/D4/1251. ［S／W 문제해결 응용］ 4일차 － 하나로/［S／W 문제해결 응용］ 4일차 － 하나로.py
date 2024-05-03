def func(start):
    global pay

    distance[start] = 0
    for _ in range(n):
        min_idx = -1
        min_val = float('inf')

        for i in range(n):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]

        visited[min_idx] = 1
        pay += e * min_val

        for i in range(n):
            if not visited[i]:
                distance[i] = min(distance[i], (x[min_idx] - x[i]) ** 2 + (y[min_idx] - y[i]) ** 2)


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    visited = [0 for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    pay = 0

    func(0)

    print(f'#{test_case} {round(pay)}')