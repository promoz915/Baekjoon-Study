import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(1, t+1):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    data = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if data == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 == data or abs(r1 - r2) == data:
            print(1)
        elif ((abs(r1 - r2) < data) and (data < r1 + r2)):
            print(2)
        else:
            print(0)