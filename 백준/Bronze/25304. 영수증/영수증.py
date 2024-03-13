a = int(input())
b = int(input())
sum = 0
for i in range(b):
    p, c = map(int, input().split())
    sum += (p * c)
    
if a == sum:
    print("Yes")
else:
    print("No")