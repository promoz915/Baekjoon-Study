import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    m.append(int(input()))
for i in sorted(m):
    print(i)