T = int(input())
for test_case in range(1, T + 1):
    data = int(input())
    print(f'#{test_case} {"Even"}') if data % 2 == 0 else print(f'#{test_case} {"Odd"}')