a, b = [], []
n, m = map(int, input().split())

for i in range(n):
    lista = list(map(int, input().split()))
    a.append(lista)

for i in range(n):
    listb = list(map(int, input().split()))
    b.append(listb)

for i in range(n):
    for j in range(m):
        result = a[i][j] + b[i][j]
        print(result, end = ' ')
    print()