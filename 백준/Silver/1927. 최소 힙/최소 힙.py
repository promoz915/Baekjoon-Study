import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(data, num)
    else:
        try:
            print(heapq.heappop(data))
        except:
            print(0)