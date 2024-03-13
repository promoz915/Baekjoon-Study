import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
numRemainder = [0] * m

for i in range(n):
    sum += A[i]
    numRemainder[sum % m] += 1

result = numRemainder[0]

for i in numRemainder:
    result += i*(i-1)//2
print(result)
