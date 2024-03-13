import sys
input = sys.stdin.readline

xarr = []
yarr = []
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    xarr.append(x)
    yarr.append(y)

print((max(xarr) - min(xarr)) * (max(yarr) - min(yarr)))