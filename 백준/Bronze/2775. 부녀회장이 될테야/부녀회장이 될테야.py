import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    floor = int(input())
    num = int(input())

    f0 = [x for x in range(1, num+1)]       # 0층 리스트 : 1호 ~ num+1호
    for k in range(floor):                  # 층수만큼 반복
        for i in range(1, num):             # 1 ~ num 까지 반복
            f0[i] += f0[i-1]                # 이전 호수 세입자 합계 계산
    print(f0[num-1])                        # for문 끝난 후 num-1호 세입자 수 계산(index 순서때문에 -1)