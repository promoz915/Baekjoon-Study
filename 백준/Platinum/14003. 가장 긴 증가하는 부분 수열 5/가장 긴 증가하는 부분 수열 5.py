import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

MOD = 1000001
idx = 0
max_len = 1
b = [0] * MOD       # 현재 가장 유리한 증가 수열 저장 리스트
d = [0] * MOD       # 0~i까지 i를 포함하는 최장 증가 수열의 길이 저장 리스트
ans = [0] * MOD
b[max_len] = a[1]
d[1] = 1

def bina(l, r, now):
    while l < r:            # l이 r과 비교했을 때 같아지거나 커지기 전까지 이진 탐색
        mid = (l+r) // 2
        if b[mid] < now:
            l = mid + 1
        else:
            r = mid
    return l

for i in range(2, n+1):
    if b[max_len] < a[i]:   # b[max_len] = a[1] 이므로, 비교하여 a[i]가 더 크다면
        max_len += 1        # 최대 길이를 늘리고
        b[max_len] = a[i]   # max_len 업데이트
        d[i] = max_len      # d[i] 업데이트
    else:
        idx = bina(1, max_len, a[i])    # 이진 탐색 이용, index 찾기
        b[idx] = a[i]       # index 값 업데이트
        d[i] = idx          # d[i] 업데이트

print(max_len)
idx = max_len               # idx를 수열 최대 길이로 저장

for i in range(n, 0, -1):   # 뒤에서부터 찾기
    if d[i] == idx:
        ans[idx] = a[i]
        idx -= 1

for i in range(1, max_len+1):
    print(ans[i], end=' ')