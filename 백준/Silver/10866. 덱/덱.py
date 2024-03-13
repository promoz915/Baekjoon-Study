import sys
from collections import deque
input = sys.stdin.readline
arr = deque()

n = int(input())
for i in range(n):
    order = input().split()
    if order[0] == 'push_front':
        arr.appendleft(order[1])
    if order[0] == 'push_back':
        arr.append(order[1])
    elif order[0] == 'pop_front':
        print(arr.popleft() if arr else -1)
    elif order[0] == 'pop_back':
        print(arr.pop() if arr else -1)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        print(1 if len(arr) == 0 else 0)
    elif order[0] == 'front':
        print(arr[0] if arr else -1)
    elif order[0] == 'back':
        print(arr[-1] if arr else -1)