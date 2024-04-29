n, m = map(int, input().split())
data = list(map(int, input().split()))

for i in range(len(data)):
    print(data[i] - (n*m), end=' ')