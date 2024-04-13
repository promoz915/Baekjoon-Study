import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = dict()

for i in range(1, n+1):
    name = str(input().strip())
    s[i] = name
    s[name] = i

for i in range(m):
    q = input().strip()
    if q.isdigit():
        print(s[int(q)])
    else:
        print(s[q])