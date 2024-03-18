import sys; input = sys.stdin.readline

n = int(input())
plus, minus = [], []                        # 양수, 음수(0포함) 리스트 생성
result = 0

for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)                    # 양수일 때
    elif num <= 0:
        minus.append(num)                   # 음수거나 0일때
    else:
        result += num                       # 1일때

plus.sort(reverse=True)                     # 내림차순 정렬
minus.sort()                                # -3, -2, -1, ... 으로 정렬

for i in range(0, len(plus), 2):            # 양수 묶음
    if i + 1 >= len(plus):                  # 2개로 묶지 못하고 하나 남았을 때
        result += plus[i]                   # 하나 남은 값 더하기
    else:
        result += (plus[i] * plus[i+1])     # 두개 값 곱하기

for i in range(0, len(minus), 2):           # 음수 묶음
    if i + 1 >= len(minus):                 # 2개로 묶지 못하고 하나 남았을 때
        result += minus[i]                  # 하나 남은 값 더하기
    else:
        result += (minus[i] * minus[i+1])   # 두개 값 곱하기

print(result)