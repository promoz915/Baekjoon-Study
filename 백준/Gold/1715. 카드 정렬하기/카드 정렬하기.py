import sys; input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()

for _ in range(n):              # 우선순위 큐에 데이터 저장
    date = int(input())
    queue.put(date)

data1 = 0
data2 = 0
sum = 0

while queue.qsize() > 1:
    data1 = queue.get()         # 데이터 1 꺼내기
    data2 = queue.get()         # 데이터 2 꺼내기
    temp = data1 + data2        # 데이터 1 + 데이터 2
    sum += temp                 # 합친 데이터 sum에 저장하기
    queue.put(temp)             # 합친 데이터 리스트에 다시 넣기

print(sum)