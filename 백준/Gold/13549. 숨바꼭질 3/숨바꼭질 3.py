import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MOD = 100001
a = [0] * MOD

def dfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(a[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i < MOD and not a[i]:
                if i == x * 2 and i != 0:
                    a[i] = a[x]
                    queue.appendleft(i)
                else:
                    a[i] = a[x] + 1
                    queue.append(i)

dfs()