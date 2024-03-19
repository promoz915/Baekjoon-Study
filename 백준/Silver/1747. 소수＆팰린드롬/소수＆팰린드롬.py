import sys; input = sys.stdin.readline
import math

# 소수 판별
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

# 팰린드롬 판별
def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

N = int(input())
while True:
    if isPrime(N) and isPalindrome(N):
        print(N)
        break
    N += 1