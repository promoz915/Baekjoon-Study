import heapq

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    heap = []
    ans = []
    for _ in range(n):
        data = list(map(int, input().split()))
        if data[0] == 1:
            heapq.heappush(heap, -data[1])
        else:
            if len(heap) > 0:
                ans.append(-heapq.heappop(heap))
            else:
                ans.append(-1)
    print(f'#{test_case}', *ans)