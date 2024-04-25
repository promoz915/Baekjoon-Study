def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

t = int(input())
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    s_list = list(map(str, input().split()))
    t_list = list(map(str, input().split()))
    temp = lcm(n, m)

    data = []
    for i in range(temp):
        data.append(s_list[i % n] + t_list[i % m])

    ans = []
    q = int(input())
    for _ in range(q):
        year = int(input())
        ans.append(data[year % temp - 1])
    answer = ' '.join(ans)
    print(f'#{test_case} {answer}') 