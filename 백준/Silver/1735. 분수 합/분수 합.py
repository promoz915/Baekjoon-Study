import sys
input = sys.stdin.readline

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

num1 = a1 * b2 + a2 * b1
num2 = b1 * b2

temp = gcd(num1, num2)
num1 //= temp
num2 //= temp

print(num1, num2)