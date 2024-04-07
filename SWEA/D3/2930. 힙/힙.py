def swap(a, b):
    heap[a], heap[b] = heap[b], heap[a]

t = int(input())
heap = [0] * 100001

for test_case in range(1, t+1):
    n = int(input())
    ans = []
    size = 0
    for _ in range(n):
        order = list(map(int, input().split()))

        if order[0] == 1:
            data = order[1]
            temp = size = size + 1
            heap[temp] = data
            while temp > 1 and heap[temp] > heap[temp // 2]:
                swap(temp, temp // 2)
                temp = temp // 2

        elif order[0] == 2:
            temp = 1
            if size == 0:
                ans.append(-1)
            else:
                ans.append(heap[temp])
                heap[temp] = heap[size]
                heap[size] = 0
                size = size - 1
                while True:
                    child = temp * 2
                    if child + 1 <= size and heap[child] < heap[child + 1]:
                        child += 1
                    if child > size or heap[child] < heap[temp]:
                        break
                    swap(temp, child)
                    temp = child

    print(f'#{test_case}', *ans)