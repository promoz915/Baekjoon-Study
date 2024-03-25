import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def append_star(LEN):
    if LEN == 1:
        return ['*']

    Stars = append_star(LEN // 3)
    L = []

    for s in Stars:
        L.append(s*3)
    for s in Stars:
        L.append(s + ' ' * (LEN//3) + s)
    for s in Stars:
        L.append(s*3)
    return L

n = int(input())
print('\n'.join(append_star(n)))