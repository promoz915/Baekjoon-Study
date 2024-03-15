import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0

for i in range(1, n+1):
    result += sum(arr[0:i])
    
print(result)