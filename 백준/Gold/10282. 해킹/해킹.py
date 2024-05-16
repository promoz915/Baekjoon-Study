import sys
input = sys.stdin.readline
import heapq

def func(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dp = [1e9] * (n+1)
    dp[start] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if dp[now] > dist:
            continue
        
        for next_node, next_cost in data[now]:
            cost = dist + next_cost
            
            if dp[next_node] > cost:
                dp[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    return dp

t = int(input())
for test_case in range(1, t+1):
    n, d, c = map(int, input().split())
    data = [[] for _ in range(n+1)]
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        data[b].append((a, s))
        
    dist = func(c)
    
    cnt, time = 0, 0
    for i in range(1, n+1):
        if dist[i] != 1e9:
            cnt += 1
            time = max(time, dist[i])
            
    print(cnt, time)