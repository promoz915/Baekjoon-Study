import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
temp = set()

for i in data:
    for j in data:
        temp.add(i+j)
        
def func():
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            if data[i] - data[j] in temp:
                return data[i]
print(func())