import sys; input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0

for i in a:
    if start < i:
        start = i                       # 레슨 최댓값을 시작 인덱스로 저장
    end += i                            # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start + end) / 2)     # 중간값
    sum = 0
    count = 0                           # 블루레이 갯수
    for i in range(n):                  # 중간값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + a[i] > middle:         # 중간값보다 더한 총합이 커진다면
            count += 1                  # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체한다는 의미
            sum = 0                     # sum 초기화
        sum += a[i]                     # sum에 현재 레슨 시간값 더하기
    if sum != 0:                        # sum이 0이 아니면 마지막 블루레이가 필요하므로 카운트 값 올리기
        count += 1
    if count > m:                       # 중간 인덱스 값으로 모든 레슨 저장 불가능
        start = middle + 1
    else:                               # 중간 인덱스 값으로 모든 레슨 저장 가능
        end = middle - 1

print(start)