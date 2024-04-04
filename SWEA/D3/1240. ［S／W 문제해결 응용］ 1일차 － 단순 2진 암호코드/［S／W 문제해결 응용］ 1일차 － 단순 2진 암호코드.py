temp = ['1011000', '1001100', '1100100', '1011110', '1100010',
            '1000110', '1111010', '1101110', '1110110', '1101000']

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ans = -1
    
    for n in range(n):
        nums = input()
        if int(nums) != 0 and ans == -1:
            nums = str(int(nums[::-1]))
            
            arr = []
            for i in range(8):
                arr.insert(0, temp.index(nums[7*i:7*i+7]))
            val = (arr[0] + arr[2]+ arr[4] + arr[6])*3 + arr[1] + arr[3] + arr[5] + arr[7]
            if val % 10 == 0:
                ans = sum(arr)
            else:
                ans = 0
    print(f'#{test_case} {ans}')