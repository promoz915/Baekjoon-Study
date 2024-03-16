import sys; input = sys.stdin.readline; sys.setrecursionlimit(10000)

n = int(input())

def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

def DFM(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFM(number * 10 + i)
                
                
DFM(2); DFM(3); DFM(5); DFM(7)