import sys
input = sys.stdin.readline

while True:
    try:
        MOD = 10000000
        x = int(input()) * MOD
        n = int(input())
        data = [int(input()) for _ in range(n)]
        data.sort()
        
        i, j = 0, n-1
        flag = False
        while i < j:
            if data[i] + data[j] == x:
                print(f'yes {data[i]} {data[j]}')
                flag = True
                break
            elif data[i] + data[j] < x:
                i += 1
            else:
                j -= 1
        if flag == False:
            print('danger')
            
    except:
        break