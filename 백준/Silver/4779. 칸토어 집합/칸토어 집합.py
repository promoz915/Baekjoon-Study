import sys; input = sys.stdin.readline

def can(n):
    if n == 1:
        return '-'

    left = can(n//3)
    center = " " * (n//3)
    return left + center + left

while True:
    try:
        n = int(input())
        ans = can(3 ** n)
        print(ans)
    except:
        break