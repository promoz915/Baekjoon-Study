n, r, c = map(int, input().split())

def func(n, row, col):
    if n == 0:
        return 0
    count = 2 * (row%2) + (col%2)
    return 4 * func(n-1, row//2, col//2) + count

print(func(n, r, c))