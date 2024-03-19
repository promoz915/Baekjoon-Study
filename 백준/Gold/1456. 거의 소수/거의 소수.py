import sys; input = sys.stdin.readline
import math

n, m = map(int, input().split())
a = [0] * (10000001)

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a)) + 1)):
    if a[i] == 0:
        continue
    for j in range(i+i, len(a), i):
        a[j] = 0

count = 0

for i in range(2, 10000001):
    if a[i] != 0:
        temp = a[i]                     # 현재 소수
        while a[i] <= m / temp:         # 현재 소수 <= m / temp
            if a[i] >= n / temp:        # 현재 소수 >= n / temp
                count += 1              # 정답값 증가
            temp = temp * a[i]          # 현재 소수
print(count)