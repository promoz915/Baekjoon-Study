import sys; input = sys.stdin.readline

n, k = map(int, input().split())
a = [0] * n
count = 0

for i in range(n):              # 리스트에 동전 가격 입력
    a[i] = int(input())

for i in range(n-1, -1, -1):    # 역순으로 반복
    if a[i] <= k:               # 현재 k보다 동전 가치가 작거나 같으면
        count += int(k / a[i])  # 동전 수 += 목표 금액 / 현재 동전 가치
        k = k % a[i]            # 목표 금액 = 목표 금액 % 현재 동전 가치
print(count)