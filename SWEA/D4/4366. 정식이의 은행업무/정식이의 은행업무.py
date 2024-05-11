t = int(input())
for test_case in range(1, t+1):
    two = list(input())
    three = list(input())
    flag = False
    
    for i in range(len(two) * 2):
        temp1 = two[:]
        temp1[i//2] = str(i%2)
        a = ''.join(temp1)
        
        for j in range(len(three) * 3):
            temp2 = three[:]
            temp2[j//3] = str(j % 3)
            b = ''.join(temp2)
            
            if int(a, 2) == int(b, 3):
                print(f'#{test_case} {int(a, 2)}')
                flag = True
                break
        if flag:
            break