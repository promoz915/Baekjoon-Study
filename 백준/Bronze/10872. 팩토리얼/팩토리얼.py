x = int(input())
result = 1
if x > 0:
    for i in range(1, x+1):
        result *= i
print(result)