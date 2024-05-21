while True:
    temp = 0
    n = int(input())
    if not n:
        break
    
    for i in range(1, n+1):
        temp += i
    
    print(temp)