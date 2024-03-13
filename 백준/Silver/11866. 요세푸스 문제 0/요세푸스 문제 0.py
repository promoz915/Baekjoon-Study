import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
arr = deque()
result = []

for i in range(1, n+1):
    arr.append(i)

while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())
    
print("<", ", ".join(map(str, result)), ">", sep="")