import sys
input = sys.stdin.readline
n = int(input())
s = dict()

for _ in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        s[name] = True
    elif state == 'leave':
        del s[name]

s = sorted(s.keys(), reverse=True)

for i in s:
    print(i)