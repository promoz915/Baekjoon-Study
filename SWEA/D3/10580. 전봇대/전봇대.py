t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    data = []
    ans = 0

    for _ in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
        if data:
            for da, db in data:
                if (a < da and b > db) or (a > da and b < db):
                    ans += 1
    print(f'#{test_case} {ans}')