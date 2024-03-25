import sys; input = sys.stdin.readline
def tower(n, a, b, c):
    if n == 1:
        print(a, c)
        return

    tower(n-1, a, c, b)
    print(a, c)
    tower(n-1, b, a, c)

n = int(input())
print(2**n-1)
tower(n, 1, 2, 3)