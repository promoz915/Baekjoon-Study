# 오일러 피
import math
import sys; input = sys.stdin.readline

n = int(input())
result = n

for p in range(2, int(math.sqrt(n)) + 1):
    if n % p == 0:                          # p가 소인수인지 확인
        result -= result / p                # 결괏값 = 결괏값 - 결괏값 / 현재값
        while n % p == 0:                   # 2^7*11이라면 2^7을 없애고 11만 남김
            n /= p
            
if n > 1:                                   # n이 마지막 소인수일 때
    result -= result / n

print(int(result))