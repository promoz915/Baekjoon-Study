import sys; input = sys.stdin.readline
import math

n, m = map(int, input().split())
a = [False] * (m-n+1)

for i in range(2, int(math.sqrt(m) + 1)):           # 2부터 m의 제곱근 사이
    pow = i * i                                     # 제곱수
    start_index = int(n/pow)                        # 최솟값/제곱수
    if n % pow != 0:                                # 나머지가 있는 경우 1을 더해 n보다 큰 제곱수에서 시작하도록 설정
        start_index += 1
    for j in range(start_index, int(m/pow)+1):      # 제곱수를 True로 변경
        a[int((j*pow)-n)] = True

count = 0

for i in range(0, m-n+1):                           # 제곱이 아닌 수 출력
    if not a[i]:
        count += 1

print(count)