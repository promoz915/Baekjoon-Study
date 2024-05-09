import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MOD = 100001
a = [0] * MOD
b = [0] * MOD

def move(s):
    data = []
    temp = s
    for _ in range(a[s] + 1):
        data.append(temp)
        temp = b[temp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(a[x])
            move(x)
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i < MOD and not a[i]:
                a[i] = a[x] + 1
                queue.append(i)
                b[i] = x

bfs()