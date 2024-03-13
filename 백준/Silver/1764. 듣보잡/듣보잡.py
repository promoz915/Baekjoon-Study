import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = []
arr1 = []
arr2 = []
for _ in range(n):
    a = str(input())
    arr1.append(a)
for _ in range(m):
    b = str(input())
    arr2.append(b)

result = list(set(arr1) & set(arr2))
result.sort()
print(len(result))
print(''.join(result), end='')