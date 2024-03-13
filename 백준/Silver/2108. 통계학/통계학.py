from collections import Counter
import sys
input = sys.stdin.readline
arr = []

n = int(input())
for _ in range(n):
    x = int(input())
    arr.append(x)
arr.sort()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])

count = Counter(arr)            # 빈도수 계산
order = count.most_common()     # 딕녀서리 형태로 수와 빈도수 저장
m = order[0][1]                 # 최대 빈도수 : values

lis = []                        # 최대 빈도수를 가진 수들을 저장하는 리스트 (같은 빈도의 수 탐색)
for i in order:
    if i[1] == m:               # 각 수의 빈도수가 최대 빈도값인 m이면
        lis.append(i[0])        # lis에 수 저장

print(lis[0] if len(lis) == 1 else lis[1])
print(max(arr) - min(arr))