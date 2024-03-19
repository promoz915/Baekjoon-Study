# 최대공약수

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
result = gcd(a, b)

while result > 0:
    print(1, end='')
    result -= 1